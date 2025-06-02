#!/usr/bin/python3
import datetime
import json
import lxml.etree
import os
import requests
import sys

from simplejson.errors import JSONDecodeError as SimpleJSONDecodeError

try:
    import logman
except ModuleNotFoundError:
    sys.path.append('.')
    sys.path.append('..')
    import logman
try:
    from scripts import globs
    from scripts import utils
except ModuleNotFoundError:
    import globs
    import utils


def get_individual_atlantsolia_prices():
    relation = globs.ATLANTSOLIA_LOCATION_RELATION
    url = 'https://www.atlantsolia.is/stodvaverd/'
    res = requests.get(url, headers=utils.headers())
    res.raise_for_status()
    html_text = res.content
    html = lxml.etree.fromstring(html_text, lxml.etree.HTMLParser())
    price_table = html.find('.//table[@class="table"]')
    price_rows = price_table.findall('.//tbody/tr')
    prices = {}
    for price_row in price_rows:
        station_name = price_row[0][0].text.strip()
        key = relation[station_name]
        bensin95 = float(price_row[1][0].text.strip().replace(',', '.'))
        diesel = float(price_row[2][0].text.strip().replace(',', '.'))
        bensin95_discount = round((bensin95 - globs.ATLANTSOLIA_MINIMUM_DISCOUNT), 1)
        diesel_discount = round((diesel - globs.ATLANTSOLIA_MINIMUM_DISCOUNT), 1)
        if key in globs.ATLANTSOLIA_DISCOUNTLESS_STATIONS:
            bensin95_discount = None
            diesel_discount = None
        prices[key] = {
            'bensin95': bensin95,
            'diesel': diesel,
            'bensin95_discount': bensin95_discount,
            'diesel_discount': diesel_discount
        }
    return prices


def get_global_costco_prices():
    # Costco does not intend to show petrol price on their webpage according to
    # email reply I've received from them, so we have no choice but to hardcode
    # their prices if we wish to include their prices in Gasvaktin.
    # Instead of hardcoding prices in the repo itself like with Dælan last
    # summer I've created a personal Google Docs Spreadsheet to hold their
    # current petrol prices, Simplifies updating prices if away from
    # workstation.
    headers = {
        'Accept': (
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,'
            '*/*;q=0.8'
        ),
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'en-US,en;q=0.8,is;q=0.6,da;q=0.4',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'User-Agent': utils.random_ua()
    }
    google_doc_url = 'https://docs.google.com/spreadsheets/d/{id}/edit'
    doc_id = '18xuZbhfInW_6Loua3_4LE7KxbGPsh-_3IFfLpf3uwYE'
    res = requests.get(google_doc_url.format(id=doc_id), headers=headers)
    res.raise_for_status()
    # <somewhat-naive-html-parsing>
    root = lxml.etree.fromstring(res.content, lxml.etree.HTMLParser())
    bensin = float(root.xpath('.//td[text()="Bensin"]')[0].getnext().text)
    diesel = float(root.xpath('.//td[text()="Diesel"]')[0].getnext().text)
    # </somewhat-naive-html-parsing>
    return {
        'bensin95': bensin,
        'diesel': diesel,
        'bensin95_discount': None,  # Costco has no discount program
        'diesel_discount': None
    }


def get_individual_n1_prices():
    url_eldsneyti = 'https://www.n1.is/thjonusta/eldsneyti/daeluverd/'
    url_eldsneyti_api = 'https://www.n1.is/umbraco/api/fuel/getfuelprices'
    headers = utils.headers()
    session = requests.Session()
    session.get(url_eldsneyti, headers=headers)
    headers_eldsneyti_api = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,is-IS;q=0.8,is;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Host': 'www.n1.is',
        'Origin': 'https://www.n1.is',
        'Referer': 'https://www.n1.is/thjonusta/eldsneyti/daeluverd/',
        'User-Agent': headers['User-Agent']
    }
    res = session.post(url_eldsneyti_api, data='', headers=headers_eldsneyti_api)
    res.raise_for_status()
    prices = {}
    def read_current_n1_prices():
        current_price_data_file = os.path.abspath(os.path.join(
            os.path.dirname(os.path.realpath(__file__)), '../vaktin/gas.min.json'
        ))
        current_price_data = utils.load_json(current_price_data_file)
        for station in current_price_data['stations']:
            if not station['key'].startswith('n1_'):
                continue
            prices[station['key']] = {
                'bensin95': station['bensin95'],
                'diesel': station['diesel'],
                'bensin95_discount': station['bensin95_discount'],
                'diesel_discount': station['diesel_discount']
            }
        return prices
    # <n1-endpoint-down-fallback>
    try:
        stations = res.json()
    except (json.JSONDecodeError, SimpleJSONDecodeError):
        # N1 price endpoint seems to be down, adding fallback to current prices to continue
        # monitoring the other companies while N1 endpoint is down.
        logman.warning('Failed querying N1 endpoint, using current N1 price data as fallback.')
        return read_current_n1_prices()
    # </n1-endpoint-down-fallback>
    names_ignore_words = [
        'Þjónustustöð/Verslun',
        'Þjónustustöð',
        'Sjálfsafgreiðslustöð',
        'Sjálfsafgreiðsla',
    ]
    current_n1_prices = None
    for station in stations:
        # <get-name>
        name = station['Name']  # sometimes a bit dirty, so we attempt to clean it up
        for word in names_ignore_words:
            name = name.replace(word, '')
        name = name.replace('-', ' ')
        name = ' '.join(name.split())
        # </get-name>
        if name == 'Flugvellir 27':
            continue
        key = globs.N1_LOCATION_RELATION[name]
        if name == 'Skútuvogi' and station['GasPrice'] is None:
            continue
        bensin95 = float(station['GasPrice'].replace(',', '.'))
        # <zero-bensin-price-fallback>
        if bensin95 == 0:
            if current_n1_prices is None:
                logman.warning('Loading current N1 price because of zero price!')
                current_n1_prices = read_current_n1_prices()
            logman.warning(f'Zero bensin price for N1 station "{key}", fallback to current price.')
            bensin95 = current_n1_prices[key]['bensin95']
        # </zero-bensin-price-fallback>
        diesel = float(station['DiselPrice'].replace(',', '.'))
        # <zero-diesel-price-fallback>
        if diesel == 0:
            if current_n1_prices is None:
                logman.warning('Loading current N1 price because of zero price!')
                current_n1_prices = read_current_n1_prices()
            logman.warning(f'Zero diesel price for N1 station "{key}", fallback to current price.')
            diesel = current_n1_prices[key]['diesel']
        # </zero-diesel-price-fallback>
        if key in globs.N1_DISCOUNTLESS_STATIONS:
            bensin95_discount = None
            diesel_discount = None
        else:
            bensin95_discount = round((bensin95 - globs.N1_DISCOUNT), 1)
            diesel_discount = round((diesel - globs.N1_DISCOUNT), 1)
        prices[key] = {
            'bensin95': bensin95,
            'diesel': diesel,
            'bensin95_discount': bensin95_discount,
            'diesel_discount': diesel_discount
        }
    return prices


def get_individual_olis_prices():
    url = 'https://ob.olis.is/_od_api/price/'
    res = requests.get(url, headers=utils.headers())
    res.raise_for_status()
    data = res.json()
    parsed = {'stations': {}}
    for entry in data['data']:
        if entry['name'] == 'PIERPUMP':
            continue
        if entry['OB'] == 1:
            continue
        station_key = globs.OLIS_LOCATION_RELATION[entry['name']]
        if station_key not in parsed['stations']:
            parsed['stations'][station_key] = {}
        if entry['type'] == 'SjalfsafgreidslaBensin95':
            parsed['stations'][station_key]['bensin95'] = entry['price']
        elif entry['type'] == 'SjalfsafgreidslaDisel':
            parsed['stations'][station_key]['diesel'] = entry['price']
        elif entry['type'] == 'SjalfsafgreidslaLitudDiesel':
            continue
        else:
            raise Exception('Unexpected type "%s"' % (entry['type'], ))
    prices = {}
    olis_stations = utils.load_json(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), '../stations/olis.json')
    )
    for key in olis_stations:
        bensin95 = parsed['stations'][key]['bensin95']
        diesel = parsed['stations'][key]['diesel']
        bensin95_discount = round((bensin95 - globs.OLIS_MINIMUM_DISCOUNT), 1)
        diesel_discount = round((diesel - globs.OLIS_MINIMUM_DISCOUNT), 1)
        prices[key] = {
            'bensin95': bensin95,
            'diesel': diesel,
            'bensin95_discount': bensin95_discount,
            'diesel_discount': diesel_discount
        }
    return prices


def get_individual_ob_prices():
    url = 'https://ob.olis.is/_od_api/price/'
    res = requests.get(url, headers=utils.headers())
    res.raise_for_status()
    data = res.json()
    parsed = {'stations': {}}
    for entry in data['data']:
        if entry['name'] == 'PIERPUMP':
            continue
        if entry['OB'] != 1:
            continue
        if entry['name'] in ['Búðardalur', 'Ketilás']:
            continue  # those stations seem to only sell diesel fuel, skip for now
        station_key = globs.OB_LOCATION_RELATION[entry['name']]
        if station_key not in parsed['stations']:
            parsed['stations'][station_key] = {}
        if entry['type'] == 'SjalfsafgreidslaBensin95':
            parsed['stations'][station_key]['bensin95'] = entry['price']
        elif entry['type'] == 'SjalfsafgreidslaDisel':
            parsed['stations'][station_key]['diesel'] = entry['price']
        elif entry['type'] == 'SjalfsafgreidslaLitudDiesel':
            continue
        else:
            raise Exception('Unexpected type "%s"' % (entry['type'], ))
    prices = {}
    ob_stations = utils.load_json(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), '../stations/ob.json')
    )
    for key in ob_stations:
        bensin95 = parsed['stations'][key]['bensin95']
        diesel = parsed['stations'][key]['diesel']
        if key not in globs.OB_DISCOUNTLESS_STATIONS:
            bensin95_discount = round((bensin95 - globs.OB_MINIMUM_DISCOUNT), 1)
            diesel_discount = round((diesel - globs.OB_MINIMUM_DISCOUNT), 1)
        else:
            bensin95_discount = None
            diesel_discount = None
        prices[key] = {
            'bensin95': bensin95,
            'diesel': diesel,
            'bensin95_discount': bensin95_discount,
            'diesel_discount': diesel_discount
        }
    return prices


def get_individual_orkan_prices():
    url = 'https://www.orkan.is/orkustodvar/'
    res = requests.get(url, headers=utils.headers(bot=True))
    res.raise_for_status()
    html = lxml.etree.fromstring(res.content.decode('utf-8'), lxml.etree.HTMLParser())
    prices_cards = html.findall('.//div[@class="prices__card"]/div[@class="prices__card-content"]')
    prices = {}
    for card in prices_cards:
        card_values = card.findall('.//div[@class="prices__price-value"]')
        station_name = card_values[0].text.strip()
        if station_name == 'Orkustöð':
            continue  # skip header row
        if 'rafhleðsla' in station_name:
            # "Selfoss rafhleðsla"
            continue  # skip electric charging stations
        bensin95 = float(card_values[1].text.strip().replace(',', '.'))
        diesel = float(card_values[2].text.strip().replace(',', '.'))
        key = globs.ORKAN_LOCATION_RELATION[station_name]
        if key not in globs.ORKAN_DISCOUNTLESS_STATIONS:
            bensin95_discount = round(bensin95 - globs.ORKAN_MINIMUM_DISCOUNT, 1)
            diesel_discount = round(diesel - globs.ORKAN_MINIMUM_DISCOUNT, 1)
        else:
            bensin95_discount = None
            diesel_discount = None
        prices[key] = {
            'bensin95': bensin95,
            'diesel': diesel,
            'bensin95_discount': bensin95_discount,
            'diesel_discount': diesel_discount
        }
    if 'or_074' not in prices:
        # new station at Lambhagavegur for some reason not shown in list, after appearing last week
        # for now we link its price to station Orkan Vesturlandsvegur in the near vicinity
        prices['or_074'] = prices['or_052'].copy()
    return prices


def testrun(selection):
    if logman.Logger is None:
        logman.init(role='cli', log_to_file=False)
    run_all = ('all' in selection)
    if run_all or 'ao' in selection:
        logman.info('Atlantsolía')
        logman.info(get_individual_atlantsolia_prices())
    if run_all or 'co' in selection:
        logman.info('Costco')
        logman.info(get_global_costco_prices())
    if run_all or 'n1' in selection:
        logman.info('N1')
        logman.info(get_individual_n1_prices())
    if run_all or 'ol' in selection:
        logman.info('Olís')
        logman.info(get_individual_olis_prices())
    if run_all or 'ob' in selection:
        logman.info('ÓB')
        logman.info(get_individual_ob_prices())
    if run_all or 'or' in selection or 'ox' in selection:
        logman.info('Orkan')
        logman.info(get_individual_orkan_prices())


if __name__ == '__main__':
    testrun(['all'])
