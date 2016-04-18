#!/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import etree
import requests

import glob, utils

def get_individual_atlantsolia_prices():
	relation = glob.ATLANTSOLIA_LOCATION_RELATION
	url = 'http://atlantsolia.is/stodvarverd.aspx'
	res = requests.get(url, headers=utils.headers())
	html_text = res.content
	# bensin95 discount, is 3 ISK when writing this but you never know
	bensin95_start_text = 'tempPrice = parseFloat($(\'#Allment95\').text().replace(",",".")) - '
	bensin95_end_text = ';'
	bensin95_start = html_text.find(bensin95_start_text) + len(bensin95_start_text)
	bensin95_end = bensin95_start + html_text[bensin95_start:].find(bensin95_end_text)
	bensin95_discount_text = html_text[bensin95_start:bensin95_end]
	# diesel discount, is 3 ISK when writing this but you never know
	diesel_start_text = 'tempPrice = parseFloat($(\'#AllmentDisel\').text().replace(",", ".")) - '
	diesel_end_text = ';'
	diesel_start = html_text.find(diesel_start_text) + len(diesel_start_text)
	diesel_end = diesel_start + html_text[bensin95_start:].find(bensin95_end_text)
	diesel_discount_text = html_text[diesel_start:diesel_end]
	discounts = {
		'bensin95': float(bensin95_discount_text),
		'diesel': float(diesel_discount_text)
	}
	# parse prices from html
	html = etree.fromstring(html_text, etree.HTMLParser())
	div_prices = html.find('.//div[@id="mainLayer"]/div[8]/div[7]')
	prices = {}
	for div_price in div_prices:
		if not div_price.values() == ['overflow:hidden']:
			continue # skip empty divs
		if div_price[1].text == '95 okt.':
			continue # skip header
		key = relation[div_price[0][0].text]
		bensin95 = float(div_price[1][0].text.replace(',','.'))
		diesel = float(div_price[2][0].text.replace(',','.'))
		prices[key] = {
			'bensin95': bensin95,
			'diesel': diesel,
			'bensin95_discount': bensin95 - discounts['bensin95'],
			'diesel_discount': diesel - discounts['diesel']
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
	res = session.post(url_eldsneyti_api, data=post_data_bensin, headers=headers_eldsneyti_api)
	bensin95_discount_text = res.content
	headers_eldsneyti_api['Content-Length'] = str(len(post_data_diesel))
	res = session.post(url_eldsneyti_api, data=post_data_diesel, headers=headers_eldsneyti_api)
	diesel_discount_text = res.content
	# prices with discount
	prices['bensin95_discount'] = float(bensin95_discount_text.replace('"','').replace(',','.'))
	prices['diesel_discount'] = float(diesel_discount_text.replace('"','').replace(',','.'))
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
		'bensin95': float(bensin95_text.replace(',','.')),
		'diesel': float(diesel_text.replace(',','.')),
		'bensin95_discount': float(bensin_discount_text.replace(',','.')),
		'diesel_discount': float(diesel_discount_text.replace(',','.'))
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
		'bensin95': float(bensin95_text.replace(',','.')),
		'diesel': float(diesel_text.replace(',','.')),
		'bensin95_discount': float(bensin_discount_text.replace(',','.')),
		'diesel_discount': float(diesel_discount_text.replace(',','.'))
	}

def get_global_skeljungur_prices():
	url = 'http://www.skeljungur.is/einstaklingar/eldsneytisverd/'
	res = requests.get(url, headers=utils.headers())
	html = etree.fromstring(res.content, etree.HTMLParser())
	bensin95_text = html.find('.//*[@id="st-container"]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div[2]/div[1]/div[2]/h2').text
	diesel_text = html.find('.//*[@id="st-container"]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div[2]/div[1]/div[4]/h2').text
	bensin95 = float(bensin95_text.replace(' kr.','').replace(',','.'))
	diesel = float(diesel_text.replace(' kr.','').replace(',','.'))
	return {
		'bensin95': bensin95,
		'diesel': diesel,
		'bensin95_discount': None, # skeljungur has no special discount stuff
		'diesel_discount': None    # (that's what their subsidiary Orkan is for)
	}

def get_global_orkan_prices():
	url = 'http://www.skeljungur.is/einstaklingar/eldsneytisverd/'
	res = requests.get(url, headers=utils.headers())
	html = etree.fromstring(res.content, etree.HTMLParser())
	bensin95_text = html.find('.//*[@id="st-container"]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div[2]/div[2]/div[2]/h2').text
	diesel_text = html.find('.//*[@id="st-container"]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div[2]/div[2]/div[4]/h2').text
	bensin95 = float(bensin95_text.replace(' kr.','').replace(',','.'))
	diesel = float(diesel_text.replace(' kr.','').replace(',','.'))
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

def get_global_orkan_x_prices():
	# Orkan X Skemmuvegi is an exception to this global price
	# Today (2016-04-17) it seems to always be 5 ISK cheaper
	url = 'http://www.skeljungur.is/einstaklingar/eldsneytisverd/'
	res = requests.get(url, headers=utils.headers())
	html = etree.fromstring(res.content, etree.HTMLParser())
	bensin95_text = html.find('.//*[@id="st-container"]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div[2]/div[3]/div[2]/h2').text
	diesel_text = html.find('.//*[@id="st-container"]/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/div/div[2]/div[3]/div[4]/h2').text
	bensin95 = float(bensin95_text.replace(' kr.','').replace(',','.'))
	diesel = float(diesel_text.replace(' kr.','').replace(',','.'))
	return {
		'bensin95': bensin95,
		'diesel': diesel,
		'bensin95_discount': None, # Orkan X has no special discount stuff
		'diesel_discount': None    # (this is suppodedly one of its trademarks)
	}

if __name__ == '__main__':
	# Some manual testing
	# TODO: add automatic tests and stuff?
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
	print get_global_orkan_x_prices()
