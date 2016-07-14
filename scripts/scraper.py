#!/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import etree
import requests

import glob
import utils


def get_individual_atlantsolia_prices():
    relation = glob.ATLANTSOLIA_LOCATION_RELATION
    url = 'http://atlantsolia.is/stodvarverd.aspx'
    res = requests.get(url, headers=utils.headers())
    html_text = res.content
    # Atlantsolía has changed their discount system to mirror Orkan
    # https://www.atlantsolia.is/daelulykill/afslattur-og-avinningur/
    # the default discount, available to all who have the Atlantsolía pump key,
    # is 3.2 ISK
    # Source:
    # https://www.atlantsolia.is/daelulykill/afslattur-og-avinningur/
    # For consistency we just use the minimum default discount
    html = etree.fromstring(html_text, etree.HTMLParser())
    div_prices = html.find(('.//*[@id="content"]/div/div/div/div[2]/div/div/'
                            'table/tbody'))
    prices = {}
    for div_price in div_prices:
        key = relation[div_price[0][0].text]
        bensin95 = float(div_price[1].text.replace(',', '.'))
        diesel = float(div_price[2].text.replace(',', '.'))
        bensin95_discount = bensin95 - glob.ATLANTSOLIA_MINIMUM_DISCOUNT
        diesel_discount = diesel - glob.ATLANTSOLIA_MINIMUM_DISCOUNT
        prices[key] = {
            'bensin95': bensin95,
            'diesel': diesel,
            'bensin95_discount': int(bensin95_discount * 10) / 10.0,
            'diesel_discount': int(diesel_discount * 10) / 10.0
        }
    return prices


def get_global_n1_prices():
    url_listaverd = 'https://www.n1.is/listaverd/'
    url_listaverd_api = 'https://www.n1.is/umbraco/api/fuel/GetListPrice'
    url_eldsneyti = 'https://www.n1.is/eldsneyti/'
    url_eldsneyti_api = 'https://www.n1.is/umbraco/api/fuel/GetSingleFuelPrice'
    headers = utils.headers()
    session = requests.Session()
    session.get(url_listaverd, headers=headers)
    headers_listaverd_api = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8,is;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Host': 'www.n1.is',
        'Origin': 'https://www.n1.is',
        'Referer': 'https://www.n1.is/listaverd/',
        'User-Agent': headers['User-Agent'],
        'X-Requested-With': 'XMLHttpRequest'
    }
    res = session.post(url_listaverd_api, headers=headers_listaverd_api)
    datas = res.json()
    prices = {}
    # prices without discount
    for data in datas:
        if data['description'] == u'Bens\xedn':
            prices['bensin95'] = float(data['price'].replace(',', '.'))
        elif data['description'] == u'D\xedsel':
            prices['diesel'] = float(data['price'].replace(',', '.'))
    session.get(url_eldsneyti, headers=headers)
    post_data_bensin = 'fuelType=95+Oktan'
    post_data_diesel = 'fuelType=D%C3%ADsel'
    headers_eldsneyti_api = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.8,is;q=0.6',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'www.n1.is',
        'Origin': 'https://www.n1.is',
        'Referer': 'https://www.n1.is/eldsneyti/',
        'User-Agent': headers['User-Agent'],
        'X-Requested-With': 'XMLHttpRequest'
    }
    headers_eldsneyti_api['Content-Length'] = str(len(post_data_bensin))
    res = session.post(url_eldsneyti_api, data=post_data_bensin,
                       headers=headers_eldsneyti_api)
    bensin95_discount_text = res.content
    headers_eldsneyti_api['Content-Length'] = str(len(post_data_diesel))
    res = session.post(url_eldsneyti_api, data=post_data_diesel,
                       headers=headers_eldsneyti_api)
    diesel_discount_text = res.content
    # prices with discount
    prices['bensin95_discount'] = float(bensin95_discount_text.replace(
                                        '"', '').replace(',', '.'))
    prices['diesel_discount'] = float(diesel_discount_text.replace(
                                      '"', '').replace(',', '.'))
    return prices


def get_global_daelan_prices():
    # Dælan currently does not expose their prices on the website
    # http://daelan.is/.
    # When asking Dælan about this the answers have been that they're working
    # on adding it to their site soon.
    # Last time I asked (2016-06-03) the answer was:
    # "Verðið í dag á Dælunni er 172,7 fyrir díselolíu og 191,7 fyrir bensín."
    # "Erum við að vinna að því að koma þeim verðum á síðuna okkar og vonandi
    # gengur það eftir í næstu viku."
    #
    # Hardcoded prices, last changed 2016-07-14
    hardcoded_bensin95 = 191.2
    hardcoded_diesel = 174.6
    return {
        'bensin95': hardcoded_bensin95,
        'diesel': hardcoded_diesel,
        # Dælan has no special discount prices
        'bensin95_discount': None,
        'diesel_discount': None
    }


def get_global_olis_prices():
    url = 'http://www.olis.is/solustadir/thjonustustodvar/eldsneytisverd/'
    res = requests.get(url, headers=utils.headers())
    html = etree.fromstring(res.content, etree.HTMLParser())
    bensin95_text = html.find('.//*[@id="gas-price"]/span[1]').text
    diesel_text = html.find('.//*[@id="gas-price"]/span[2]').text
    bensin_discount_text = html.find('.//*[@id="gas-price"]/span[4]').text
    diesel_discount_text = html.find('.//*[@id="gas-price"]/span[5]').text
    return {
        'bensin95': float(bensin95_text.replace(',', '.')),
        'diesel': float(diesel_text.replace(',', '.')),
        'bensin95_discount': float(bensin_discount_text.replace(',', '.')),
        'diesel_discount': float(diesel_discount_text.replace(',', '.'))
    }


def get_global_ob_prices():
    url = 'http://www.ob.is/eldsneytisverd/'
    res = requests.get(url, headers=utils.headers())
    html = etree.fromstring(res.content, etree.HTMLParser())
    bensin95_text = html.find('.//*[@id="gas-price"]/span[1]').text
    diesel_text = html.find('.//*[@id="gas-price"]/span[2]').text
    bensin_discount_text = html.find('.//*[@id="gas-price"]/span[3]').text
    diesel_discount_text = html.find('.//*[@id="gas-price"]/span[4]').text
    return {
        'bensin95': float(bensin95_text.replace(',', '.')),
        'diesel': float(diesel_text.replace(',', '.')),
        'bensin95_discount': float(bensin_discount_text.replace(',', '.')),
        'diesel_discount': float(diesel_discount_text.replace(',', '.'))
    }


def get_global_skeljungur_prices():
    url = 'http://www.skeljungur.is/einstaklingar/eldsneytisverd/'
    res = requests.get(url, headers=utils.headers())
    html = etree.fromstring(res.content, etree.HTMLParser())
    bensin95_text = html.find(('.//*[@id="st-container"]/div/div/div/div/'
                               'div[2]/div/div/div[1]/div[1]/div[1]/section/'
                               'div/div[2]/div[1]/div[2]/h2')).text
    diesel_text = html.find(('.//*[@id="st-container"]/div/div/div/div/div[2]/'
                             'div/div/div[1]/div[1]/div[1]/section/div/div[2]/'
                             'div[1]/div[4]/h2')).text
    bensin95 = float(bensin95_text.replace(' kr.', '').replace(',', '.'))
    diesel = float(diesel_text.replace(' kr.', '').replace(',', '.'))
    return {
        'bensin95': bensin95,
        'diesel': diesel,
        'bensin95_discount': None,  # skeljungur has no special discount stuff
        'diesel_discount': None  # (that's what their subsidiary Orkan is for)
    }


def get_global_orkan_prices():
    url = 'http://www.skeljungur.is/einstaklingar/eldsneytisverd/'
    res = requests.get(url, headers=utils.headers())
    html = etree.fromstring(res.content, etree.HTMLParser())
    bensin95_text = html.find(('.//*[@id="st-container"]/div/div/div/div/'
                               'div[2]/div/div/div[1]/div[1]/div[1]/section/'
                               'div/div[2]/div[2]/div[2]/h2')).text
    diesel_text = html.find(('.//*[@id="st-container"]/div/div/div/div/div[2]/'
                             'div/div/div[1]/div[1]/div[1]/section/div/div[2]/'
                             'div[2]/div[4]/h2')).text
    bensin95 = float(bensin95_text.replace(' kr.', '').replace(',', '.'))
    diesel = float(diesel_text.replace(' kr.', '').replace(',', '.'))
    # Orkan has a 3-step discount system controlled by your spendings on
    # gas from them the month before
    # See more info here: https://www.orkan.is/Afslattarthrep
    # For consistency we just use the minimum default discount
    bensin95_discount = bensin95 - glob.ORKAN_MINIMUM_DISCOUNT
    diesel_discount = diesel - glob.ORKAN_MINIMUM_DISCOUNT
    return {
        'bensin95': bensin95,
        'diesel': diesel,
        'bensin95_discount': bensin95_discount,
        'diesel_discount': diesel_discount
    }


def get_individual_orkan_x_prices():
    url = 'http://www.orkan.is/Orkan-X/Stodvar'
    res = requests.get(url, headers=utils.headers())
    html = etree.fromstring(res.content, etree.HTMLParser())
    table = html.find('.//*[@id="content"]/div/div[2]/div/table')
    prices = {}
    # Issue: it has come up that prices are missing for station in this list,
    #        I sent Orkan X a line about this last friday (2016-06-03), their
    #        reply was:
    #        "takk fyrir að láta okkur vita við kippum þessu i lag :)"
    #        still not fixed
    # Solution: let's assume a station with missing prices has the highest
    # prices shown for other stations in the list
    # <find_highest_prices>
    highest_bensin95 = None
    highest_diesel = None
    for column in table:
        if column[0].text == 'Orkan X':
            continue  # skip header
        if column[1].text is not None:
            bensin95 = float(column[1].text.replace(',', '.'))
            if highest_bensin95 is None or highest_bensin95 < bensin95:
                highest_bensin95 = bensin95
        if column[2].text is not None:
            diesel = float(column[2].text.replace(',', '.'))
            if highest_diesel is None or highest_diesel < diesel:
                highest_diesel = diesel
    assert(highest_bensin95 is not None)
    assert(highest_diesel is not None)
    # </find_highest_prices>
    for column in table:
        if column[0].text == 'Orkan X':
            continue  # skip header
        key = glob.ORKAN_X_LOCATION_RELATION[column[0][0].text]
        if column[1].text is not None:
            bensin95 = float(column[1].text.replace(',', '.'))
        else:
            bensin95 = highest_bensin95
        if column[2].text is not None:
            diesel = float(column[2].text.replace(',', '.'))
        else:
            bensin95 = highest_diesel
        prices[key] = {
            'bensin95': bensin95,
            'diesel': diesel,
            # Orkan X has no special discount prices
            'bensin95_discount': None,
            'diesel_discount': None
        }
    return prices

if __name__ == '__main__':
    # Some manual testing
    # TODO: add automatic tests?
    print 'Testing scrapers\n'
    print 'Atlantsolía'
    print get_individual_atlantsolia_prices()
    print 'N1'
    print get_global_n1_prices()
    print 'Olís'
    print get_global_olis_prices()
    print 'ÓB'
    print get_global_ob_prices()
    print 'Skeljungur'
    print get_global_skeljungur_prices()
    print 'Orkan'
    print get_global_orkan_prices()
    print 'Orkan X'
    print get_individual_orkan_x_prices()
