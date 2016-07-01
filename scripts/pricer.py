#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import glob
import scraper
import utils


def main():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    companies = [
        {
            'name': glob.ATLANTSOLIA,
            'stations': '../stations/atlantsolia.json'
        },
        {
            'name': glob.N1,
            'stations': '../stations/n1.json'
        },
        {
            'name': glob.DAELAN,
            'stations': '../stations/daelan.json'
        },
        {
            'name': glob.OB,
            'stations': '../stations/ob.json'
        },
        {
            'name': glob.OLIS,
            'stations': '../stations/olis.json'
        },
        {
            'name': glob.ORKAN,
            'stations': '../stations/orkan.json'
        },
        {
            'name': glob.ORKAN_X,
            'stations': '../stations/orkanx.json'
        },
        {
            'name': glob.SKELJUNGUR,
            'stations': '../stations/skeljungur.json'
        }
    ]

    all_stations = {}
    for company in companies:
        filepath = os.path.join(current_dir, company['stations'])
        stations = utils.load_json(filepath)
        for key in stations:
            station = stations[key]
            station['company'] = company['name']
            all_stations[key] = station

    # station prices
    atlantsolia_prices = scraper.get_individual_atlantsolia_prices()
    n1_prices = scraper.get_global_n1_prices()
    daelan_prices = scraper.get_global_daelan_prices()
    ob_prices = scraper.get_global_ob_prices()
    olis_prices = scraper.get_global_olis_prices()
    orkan_prices = scraper.get_global_orkan_prices()
    orkan_x_prices = scraper.get_individual_orkan_x_prices()
    skeljungur_prices = scraper.get_global_skeljungur_prices()

    list_of_stations = []

    for key, station in sorted(all_stations.items()):
        station['key'] = key
        if station['company'] == glob.ATLANTSOLIA:
            station['bensin95'] = atlantsolia_prices[key]['bensin95']
            station['bensin95_discount'] = (
                atlantsolia_prices[key]['bensin95_discount'])
            station['diesel'] = atlantsolia_prices[key]['diesel']
            station['diesel_discount'] = (
                atlantsolia_prices[key]['diesel_discount'])
        elif station['company'] == glob.N1:
            station['bensin95'] = n1_prices['bensin95']
            station['bensin95_discount'] = n1_prices['bensin95_discount']
            station['diesel'] = n1_prices['diesel']
            station['diesel_discount'] = n1_prices['diesel_discount']
        elif station['company'] == glob.DAELAN:
            station['bensin95'] = daelan_prices['bensin95']
            station['bensin95_discount'] = daelan_prices['bensin95_discount']
            station['diesel'] = daelan_prices['diesel']
            station['diesel_discount'] = daelan_prices['diesel_discount']
        elif station['company'] == glob.OB:
            station['bensin95'] = ob_prices['bensin95']
            station['bensin95_discount'] = ob_prices['bensin95_discount']
            station['diesel'] = ob_prices['diesel']
            station['diesel_discount'] = ob_prices['diesel_discount']
        elif station['company'] == glob.OLIS:
            station['bensin95'] = olis_prices['bensin95']
            station['bensin95_discount'] = olis_prices['bensin95_discount']
            station['diesel'] = olis_prices['diesel']
            station['diesel_discount'] = olis_prices['diesel_discount']
        elif station['company'] == glob.ORKAN:
            station['bensin95'] = orkan_prices['bensin95']
            station['bensin95_discount'] = orkan_prices['bensin95_discount']
            station['diesel'] = orkan_prices['diesel']
            station['diesel_discount'] = orkan_prices['diesel_discount']
        elif station['company'] == glob.ORKAN_X:
            station['bensin95'] = orkan_x_prices[key]['bensin95']
            station['bensin95_discount'] = (
                orkan_x_prices[key]['bensin95_discount'])
            station['diesel'] = orkan_x_prices[key]['diesel']
            station['diesel_discount'] = orkan_x_prices[key]['diesel_discount']
        elif station['company'] == glob.SKELJUNGUR:
            station['bensin95'] = skeljungur_prices['bensin95']
            station['bensin95_discount'] = (
                skeljungur_prices['bensin95_discount'])
            station['diesel'] = skeljungur_prices['diesel']
            station['diesel_discount'] = skeljungur_prices['diesel_discount']
        list_of_stations.append(station)

    data = {'stations': list_of_stations}

    data_json_pretty_file = os.path.join(current_dir, '../vaktin/gas.json')
    data_minified_pretty_file = os.path.join(current_dir,
                                             '../vaktin/gas.min.json')

    utils.save_to_json(data_json_pretty_file, data, pretty=True)
    utils.save_to_json(data_minified_pretty_file, data, pretty=False)

if __name__ == '__main__':
    main()
