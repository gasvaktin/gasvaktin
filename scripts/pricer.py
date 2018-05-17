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
            'name': glob.COSTCO,
            'stations': '../stations/costco.json'
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
    costco_prices = scraper.get_global_costco_prices()
    n1_prices = scraper.get_global_n1_prices()
    daelan_prices = scraper.get_individual_daelan_prices()
    ob_prices = scraper.get_individual_ob_prices()
    olis_prices = scraper.get_global_olis_prices()
    orkan_prices = scraper.get_individual_orkan_prices()

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
        if station['company'] == glob.COSTCO:
            station['bensin95'] = costco_prices['bensin95']
            station['bensin95_discount'] = costco_prices['bensin95_discount']
            station['diesel'] = costco_prices['diesel']
            station['diesel_discount'] = costco_prices['diesel_discount']
        elif station['company'] == glob.N1:
            station['bensin95'] = n1_prices['bensin95']
            station['bensin95_discount'] = n1_prices['bensin95_discount']
            station['diesel'] = n1_prices['diesel']
            station['diesel_discount'] = n1_prices['diesel_discount']
            if key == 'n1_006':
                # N1 station in Storihjalli, near Skemmuvegur in Reykjavik
                # irl observation tells us the fuel price there is 8 ISK
                # cheaper than their global price.
                # At some point N1 added the following comment to their global
                # one price webpage:
                #
                #     https://www.n1.is/thjonusta/eldsneyti
                #     "* algengasta sjalfsafgreidsluverdid"
                #
                # meaning this one global price might not be the case on all
                # N1 stations, I'd like to see N1 then move from showing one
                # global price to show individual prices for stations or list
                # stations that have different prices than the global one,
                # this is a matter of transparency to N1 customers.
                station['bensin95'] -= 8.0
                station['bensin95_discount'] -= 8.0
                station['diesel'] -= 8.0
                station['diesel_discount'] -= 8.0
                # Note: this above price "fix" is bad and will very likely
                # become wrong in near future, however, I believe it to be a
                # good thing to add this for now.
        elif station['company'] == glob.DAELAN:
            station['bensin95'] = daelan_prices[key]['bensin95']
            station['bensin95_discount'] = (
                daelan_prices[key]['bensin95_discount'])
            station['diesel'] = daelan_prices[key]['diesel']
            station['diesel_discount'] = daelan_prices[key]['diesel_discount']
        elif station['company'] == glob.OB:
            station['bensin95'] = ob_prices[key]['bensin95']
            station['bensin95_discount'] = ob_prices[key]['bensin95_discount']
            station['diesel'] = ob_prices[key]['diesel']
            station['diesel_discount'] = ob_prices[key]['diesel_discount']
        elif station['company'] == glob.OLIS:
            station['bensin95'] = olis_prices['bensin95']
            station['bensin95_discount'] = olis_prices['bensin95_discount']
            station['diesel'] = olis_prices['diesel']
            station['diesel_discount'] = olis_prices['diesel_discount']
        elif station['company'] == glob.ORKAN:
            station['bensin95'] = orkan_prices[key]['bensin95']
            station['bensin95_discount'] = (
                orkan_prices[key]['bensin95_discount'])
            station['diesel'] = orkan_prices[key]['diesel']
            station['diesel_discount'] = orkan_prices[key]['diesel_discount']
        elif station['company'] == glob.ORKAN_X:
            station['bensin95'] = orkan_prices[key]['bensin95']
            station['bensin95_discount'] = (
                orkan_prices[key]['bensin95_discount'])
            station['diesel'] = orkan_prices[key]['diesel']
            station['diesel_discount'] = orkan_prices[key]['diesel_discount']
        list_of_stations.append(station)

    data = {'stations': list_of_stations}

    data_json_pretty_file = os.path.join(current_dir, '../vaktin/gas.json')
    data_json_mini_file = os.path.join(current_dir, '../vaktin/gas.min.json')

    utils.save_to_json(data_json_pretty_file, data, pretty=True)
    utils.save_to_json(data_json_mini_file, data, pretty=False)


if __name__ == '__main__':
    main()
