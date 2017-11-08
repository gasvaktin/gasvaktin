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
    html = etree.fromstring(html_text, etree.HTMLParser())
    div_prices = html.find(('.//*[@id="content"]/div/div/div/div[2]/div/div/'
                            'table/tbody'))
    prices = {}
    for div_price in div_prices:
        key = relation[div_price[0][0].text]
        bensin95 = float(div_price[1][0].text.replace(',', '.'))
        diesel = float(div_price[2][0].text.replace(',', '.'))
        bensin95_discount = bensin95 - glob.ATLANTSOLIA_MINIMUM_DISCOUNT
        diesel_discount = diesel - glob.ATLANTSOLIA_MINIMUM_DISCOUNT
        prices[key] = {
            'bensin95': bensin95,
            'diesel': diesel,
            'bensin95_discount': int(bensin95_discount * 10) / 10.0,
            'diesel_discount': int(diesel_discount * 10) / 10.0
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
    url = (
        'https://docs.google.com/spreadsheets/d/'
        '18xuZbhfInW_6Loua3_4LE7KxbGPsh-_3IFfLpf3uwYE/edit'
    )
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    # <shameless-incredibly-naive-html-parsing>
    bensin = None
    diesel = None
    html_text = res.content
    for line in html_text.split('\n'):
        if line.startswith(' Bensin,'):
            bensin = float(line[8:].replace(' ', ''))
        if line.startswith(' Diesel,'):
            diesel = float(line[8:].replace(' ', ''))
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
        # Costco has no discount program
        'bensin95_discount': None,
        'diesel_discount': None
    }


def get_global_n1_prices():
    url_eldsneyti = 'https://www.n1.is/eldsneyti/'
    url_eldsneyti_api = 'https://www.n1.is/umbraco/api/fuel/GetSingleFuelPrice'
    headers = utils.headers()
    session = requests.Session()
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
    prices = {}
    prices['bensin95'] = float(
        bensin95_discount_text.replace('"', '').replace(',', '.'))
    prices['diesel'] = float(
        diesel_discount_text.replace('"', '').replace(',', '.'))
    prices['bensin95_discount'] = prices['bensin95'] - glob.N1_DISCOUNT
    prices['diesel_discount'] = prices['diesel'] - glob.N1_DISCOUNT
    return prices


def get_individual_daelan_prices():
    relation = glob.DAELAN_LOCATION_RELATION
    headers = utils.headers()
    session = requests.Session()
    session.get('http://daelan.is/', headers=headers)
    session.get('https://www.n1.is/', headers=headers)
    price_endpoint = 'https://www.n1.is/umbraco/api/Fuel/GetFuelPriceForDaelan'
    res = session.get(price_endpoint, headers=headers)
    res.raise_for_status()
    stations = res.json()
    prices = {}
    for station in stations:
        assert('location' in station)
        assert('gasPrice' in station)
        assert('diselPrice' in station)
        key = relation[station['location']]
        prices[key] = {
            'bensin95': float(station['gasPrice'].replace(',', '.')),
            'diesel': float(station['diselPrice'].replace(',', '.')),
            # Dælan has no discount program
            'bensin95_discount': None,
            'diesel_discount': None
        }
    return prices


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
        'bensin95_discount': bensin95 - glob.SKELJUNGUR_DISCOUNT,
        'diesel_discount': diesel - glob.SKELJUNGUR_DISCOUNT
    }


def get_individual_orkan_prices():
    # reads prices for Orkan and Orkan X stations because they're now on the
    # same webpage
    url = 'https://www.orkan.is/Orkustodvar'
    res = requests.get(url, headers=utils.headers())
    html = etree.fromstring(res.content, etree.HTMLParser())
    div_table = html.find('.//*[@id="content"]/div/div[2]/div/div[2]')
    prices = {}
    key = None
    for element in div_table:
        element_class = element.get('class')
        if element_class.startswith('petrol-station'):
            if element[0].text in glob.ORKAN_LOCATION_RELATION:
                key = glob.ORKAN_LOCATION_RELATION[element[0].text]
            elif element[0].text in glob.ORKAN_X_LOCATION_RELATION:
                key = glob.ORKAN_X_LOCATION_RELATION[element[0].text]
            else:
                continue
        if element_class.startswith('general'):
            bensin95 = float(element[0].text.replace(',', '.'))
            diesel = float(element[1].text.replace(',', '.'))
            # Orkan X stations have keys starting with "ox", while ordinary
            # Orkan statins have keys starting with "or"
            bensin95_discount = None
            diesel_discount = None
            if key.startswith('or'):
                # Orkan has a 3-step discount system controlled by your
                # spendings on gas from them the month before
                # See more info here: https://www.orkan.is/Afslattarthrep
                # For consistency we just use the minimum default discount
                bensin95_discount = bensin95 - glob.ORKAN_MINIMUM_DISCOUNT
                diesel_discount = diesel - glob.ORKAN_MINIMUM_DISCOUNT
            prices[key] = {
                'bensin95': bensin95,
                'diesel': diesel,
                'bensin95_discount': bensin95_discount,
                'diesel_discount': diesel_discount
            }
    return prices


if __name__ == '__main__':
    print 'Testing scrapers\n'
    print 'Atlantsolía'
    print get_individual_atlantsolia_prices()
    print 'Costco'
    print get_global_costco_prices()
    print 'Dælan'
    print get_individual_daelan_prices()
    print 'N1'
    print get_global_n1_prices()
    print 'Olís'
    print get_global_olis_prices()
    print 'ÓB'
    print get_global_ob_prices()
    print 'Skeljungur'
    print get_global_skeljungur_prices()
    print 'Orkan (including Orkan X)'
    print get_individual_orkan_prices()
