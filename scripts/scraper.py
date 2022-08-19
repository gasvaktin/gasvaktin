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
    html_text = res.content
    html = lxml.etree.fromstring(html_text, lxml.etree.HTMLParser())
    div_prices = html.find('.//*[@id="content"]/div/div/div/div[2]/div/div/table/tbody')
    prices = {}
    for div_price in div_prices:
        key = relation[div_price[0][0].text]
        bensin95 = float(div_price[1][0].text.replace(',', '.'))
        diesel = float(div_price[2][0].text.replace(',', '.'))
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
    # <shameless-incredibly-naive-html-parsing>
    bensin = None
    diesel = None
    html_text = res.content.decode('utf-8')
    for line in html_text.split('\n'):
        if line.lstrip().startswith('Bensin,'):
            bensin = float(line.lstrip()[7:].replace(' ', ''))
        if line.lstrip().startswith('Diesel,'):
            diesel = float(line.lstrip()[7:].replace(' ', ''))
        if bensin is not None and diesel is not None:
            break
    if bensin is None or diesel is None:
        err_msg = 'Failed to read costco prices (%s, %s)\n%s ...' % (
            bensin,
            diesel,
            html_text[:10000]
        )
        raise Exception(err_msg)
    # </shameless-incredibly-naive-html-parsing>
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
    # <n1_endpoint_down_fallback>
    try:
        stations = res.json()
    except (json.JSONDecodeError, SimpleJSONDecodeError):
        # 2021-04-01: N1 price endpoint seems to be down, adding fallback to current prices to
        # continue monitoring the other companies while N1 endpoint is down.
        logman.warning('Failed querying N1 endpoint, using current N1 price data as fallback.')
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
    # </n1_endpoint_down_fallback>
    names_ignore_words = [
        'Þjónustustöð/Verslun',
        'Þjónustustöð',
        'Sjálfsafgreiðslustöð',
        'Sjálfsafgreiðsla'
    ]
    for station in stations:
        # <get-name>
        name = station['Name']  # sometimes a bit dirty, so we attempt to clean it up
        for word in names_ignore_words:
            name = name.replace(word, '')
        name = name.replace('-', ' ')
        name = ' '.join(name.split())
        # </get-name>
        key = globs.N1_LOCATION_RELATION[name]
        if name == 'Mývatn' and station['GasPrice'] is None:
            continue
        bensin95 = float(station['GasPrice'].replace(',', '.'))
        diesel = float(station['DiselPrice'].replace(',', '.'))
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
    # <zero-price-problem>
    # problem: a station is listed with 0 ISK price, solution: assume most frequent price instead
    # find most frequent bensin and diesel price
    price_frequency = {'bensin': {}, 'diesel': {}}
    for key in prices:
        # bensin
        bensin_price_key = str(prices[key]['bensin95'])
        if bensin_price_key not in price_frequency['bensin']:
            price_frequency['bensin'][bensin_price_key] = 0
        price_frequency['bensin'][bensin_price_key] += 1
        # diesel
        diesel_price_key = str(prices[key]['diesel'])
        if diesel_price_key not in price_frequency['diesel']:
            price_frequency['diesel'][diesel_price_key] = 0
        price_frequency['diesel'][diesel_price_key] += 1
    # most frequent prices
    most_frequent_bensin_price = float(max(price_frequency['bensin']))
    most_frequent_diesel_price = float(max(price_frequency['diesel']))
    for key in prices:
        if prices[key]['bensin95'] == 0.0:
            logman.warning('N1 bensin zero price for key "%s", using fallback.' % (key, ))
            prices[key]['bensin95'] = most_frequent_bensin_price
            prices[key]['bensin95_discount'] = round(
                (most_frequent_bensin_price - globs.N1_DISCOUNT), 1
            )
        if prices[key]['diesel'] == 0.0:
            logman.warning('N1 diesel zero price for key "%s", using fallback.' % (key, ))
            prices[key]['diesel'] = most_frequent_diesel_price
            prices[key]['diesel_discount'] = round(
                (most_frequent_diesel_price - globs.N1_DISCOUNT), 1
            )
    # </zero-price-problem>
    # <stórihjalli-station-missing>
    # dunno why, still open and known minor yet considerable price deviant, anchoring price to a
    # hardcoded deviance from most frequent price based on real world observations.
    if 'n1_006' not in prices:
        bensin95 = round((most_frequent_bensin_price - 13), 1)
        bensin95_discount = round((bensin95 - globs.N1_DISCOUNT), 1)
        diesel = round((most_frequent_diesel_price - 5), 1)
        diesel_discount = round((diesel - globs.N1_DISCOUNT), 1)
        logman.warning('N1 Stórihjalli station missing, using hardcoded deviance fallback.')
        prices['n1_006'] = {
            'bensin95': bensin95,
            'diesel': diesel,
            'bensin95_discount': bensin95_discount,
            'diesel_discount': diesel_discount
        }
    # </stórihjalli-station-missing>
    return prices


def get_individual_olis_prices():
    url = 'https://www.olis.is/solustadir/thjonustustodvar/eldsneytisverd/'
    res = requests.get(url, headers=utils.headers())
    html = lxml.etree.fromstring(res.content.decode('utf-8'), lxml.etree.HTMLParser())
    data = {
        'stations': {},
        'highest': {'bensin95': None, 'diesel': None}
    }
    price_table = html.find('.//table')  # theres just one table element, let's use that ofc
    if price_table is None:
        error_msg = 'Ekki tókst að sækja eldsneytisverð. Vinsamlega reyndu aftur síðar.'
        if error_msg in res.content.decode('utf-8'):
            # 2022-08-19: Olís price page broken
            # fallback to current prices until this is fixed
            logman.warning('Olís price page broken, using current Olís price data as fallback.')
            current_price_data_file = os.path.abspath(os.path.join(
                os.path.dirname(os.path.realpath(__file__)), '../vaktin/gas.min.json'
            ))
            prices = {}
            current_price_data = utils.load_json(current_price_data_file)
            for station in current_price_data['stations']:
                if not station['key'].startswith('ol_'):
                    continue
                prices[station['key']] = {
                    'bensin95': station['bensin95'],
                    'diesel': station['diesel'],
                    'bensin95_discount': station['bensin95_discount'],
                    'diesel_discount': station['diesel_discount']
                }
            return prices
    for row in price_table.findall('.//tr'):
        if len(row.findall('.//td')) < 3:
            continue
        if row.findall('.//td')[0].text.strip() == '':
            continue
        name = row.findall('.//td')[0].text.strip()
        station_key = globs.OLIS_LOCATION_RELATION[name]
        bensin = None
        if row.findall('.//td')[1].text.strip() != '':
            bensin = float(row.findall('.//td')[1].text.strip().replace(',', '.'))
        diesel = None
        if row.findall('.//td')[2].text.strip() != '':
            diesel = float(row.findall('.//td')[2].text.strip().replace(',', '.'))
        data['stations'][station_key] = {'bensin95': bensin, 'diesel': diesel}
        if data['highest']['bensin95'] is None or data['highest']['bensin95'] < bensin:
            data['highest']['bensin95'] = bensin
        if data['highest']['diesel'] is None or data['highest']['diesel'] < diesel:
            data['highest']['diesel'] = diesel
    assert(data['highest']['bensin95'] is not None)
    assert(data['highest']['diesel'] is not None)
    for name in data['stations']:
        # fallback to highest provided price if for some reason it's not provided ._.
        if data['stations'][name]['bensin95'] is None:
            data['stations'][name]['bensin95'] = data['highest']['bensin95']
        if data['stations'][name]['diesel'] is None:
            data['stations'][name]['diesel'] = data['highest']['diesel']
    prices = {}
    olis_stations = utils.load_json(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            '../stations/olis.json'
        )
    )
    for key in olis_stations:
        if key in data['stations']:
            bensin95 = data['stations'][key]['bensin95']
            diesel = data['stations'][key]['diesel']
        else:
            bensin95 = data['highest']['bensin95']
            diesel = data['highest']['diesel']
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
    url = 'https://www.ob.is/eldsneytisverd/'
    res = requests.get(url, headers=utils.headers())
    html = lxml.etree.fromstring(res.content.decode('utf-8'), lxml.etree.HTMLParser())
    data = {
        'stations': {},
        'highest': {'bensin95': None, 'diesel': None}
    }
    price_table = html.find('.//table[@id="gas-prices"]')
    if price_table is None:
        error_msg = 'Ekki tókst að sækja eldsneytisverð. Vinsamlega reyndu aftur síðar.'
        if error_msg in res.content.decode('utf-8'):
            # 2022-08-19: ÓB price page broken
            # fallback to current prices until this is fixed
            logman.warning('ÓB price page broken, using current ÓB price data as fallback.')
            current_price_data_file = os.path.abspath(os.path.join(
                os.path.dirname(os.path.realpath(__file__)), '../vaktin/gas.min.json'
            ))
            prices = {}
            current_price_data = utils.load_json(current_price_data_file)
            for station in current_price_data['stations']:
                if not station['key'].startswith('ob_'):
                    continue
                prices[station['key']] = {
                    'bensin95': station['bensin95'],
                    'diesel': station['diesel'],
                    'bensin95_discount': station['bensin95_discount'],
                    'diesel_discount': station['diesel_discount']
                }
            return prices
    for row in price_table.findall('.//tr'):
        if len(row.findall('.//td')) == 0:
            continue
        if row.findall('.//td')[0].get('style') == 'border:0px;':
            continue
        name = row.findall('.//td')[0].text.strip()
        if name == 'Ketilás í Fljótum':
            continue  # throw this one for now, only diesel, needs investigation
        if name == 'Keflavíkurflugvöllur':
            continue  # tempfix
        if name == 'Akranes, Umboð':
            continue  # tempfix
        station_key = globs.OB_LOCATION_RELATION[name]
        bensin = float(row.findall('.//td')[1].text.strip().replace(',', '.'))
        diesel = float(row.findall('.//td')[2].text.strip().replace(',', '.'))
        data['stations'][station_key] = {'bensin95': bensin, 'diesel': diesel}
        if data['highest']['bensin95'] is None or data['highest']['bensin95'] < bensin:
            data['highest']['bensin95'] = bensin
        if data['highest']['diesel'] is None or data['highest']['diesel'] < diesel:
            data['highest']['diesel'] = diesel
    prices = {}
    ob_stations = utils.load_json(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            '../stations/ob.json'
        )
    )
    now = datetime.datetime.now()
    end = datetime.datetime.strptime(globs.OB_EXTRA_DISCOUNT_UNTIL, '%Y-%m-%dT%H:%M')
    for key in ob_stations:
        if key in data['stations']:
            bensin95 = data['stations'][key]['bensin95']
            diesel = data['stations'][key]['diesel']
        else:
            bensin95 = data['highest']['bensin95']
            diesel = data['highest']['diesel']
        bensin95_discount = round((bensin95 - globs.OB_MINIMUM_DISCOUNT), 1)
        diesel_discount = round((diesel - globs.OB_MINIMUM_DISCOUNT), 1)
        if key in globs.OB_DISCOUNTLESS_STATIONS:
            bensin95_discount = None
            diesel_discount = None
        if key in globs.OB_EXTRA_DISCOUNT_STATIONS and now < end:
            if bensin95_discount is not None:
                bensin95_discount = round((bensin95 - globs.OB_EXTRA_DISCOUNT_AMOUNT), 1)
            if diesel_discount is not None:
                diesel_discount = round((diesel - globs.OB_EXTRA_DISCOUNT_AMOUNT), 1)
        prices[key] = {
            'bensin95': bensin95,
            'diesel': diesel,
            'bensin95_discount': bensin95_discount,
            'diesel_discount': diesel_discount
        }
    return prices


def get_individual_orkan_prices():
    url = 'https://www.orkan.is/orkustodvar/'
    res = requests.get(url, headers=utils.headers())
    html = lxml.etree.fromstring(res.content.decode('utf-8'), lxml.etree.HTMLParser())
    div_element = html.find('.//div[@class="accordion__container"]')
    territories = div_element.findall('.//div[@class="accordion__child"]')
    prices = {}
    key = None
    for territory in territories:
        for station in territory:
            station_name = station[0].text.strip()
            bensin95 = float(station[1].text.replace(',', '.').replace(' jamm', ''))
            diesel = float(station[2].text.replace(',', '.').replace(' jamm', ''))
            key = globs.ORKAN_LOCATION_RELATION[station_name]
            # Orkan has a 3-step discount system controlled by your
            # spendings on gas from them the month before
            # See more info here: https://www.orkan.is/Afslattarthrep
            # For consistency we just use the minimum default discount
            bensin95_discount = round(bensin95 - globs.ORKAN_MINIMUM_DISCOUNT, 1)
            diesel_discount = round(diesel - globs.ORKAN_MINIMUM_DISCOUNT, 1)
            if key in globs.ORKAN_DISCOUNTLESS_STATIONS:
                bensin95_discount = None
                diesel_discount = None
            prices[key] = {
                'bensin95': bensin95,
                'diesel': diesel,
                'bensin95_discount': bensin95_discount,
                'diesel_discount': diesel_discount
            }
    if 'or_070' not in prices:
        # Haedarsmari missing from webpage, irl price indicates discountless station, nowever irl
        # price does not match the other discountless Orkan stations though, so we're hardcoding a
        # fixed price based on another discountless station for now ..
        prices['or_070'] = prices['or_048'].copy()
        prices['or_070']['bensin95'] = round(prices['or_070']['bensin95'] + 3.1, 1)
        prices['or_070']['diesel'] = round(prices['or_070']['diesel'] + 3.4, 1)
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
