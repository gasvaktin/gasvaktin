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
    prices_map = {
        glob.ATLANTSOLIA: {
            'data': atlantsolia_prices,
            'type': glob.PRICETYPE.INDIVIDUAL
        },
        glob.COSTCO: {
            'data': costco_prices,
            'type': glob.PRICETYPE.GLOBAL
        },
        glob.N1: {
            'data': n1_prices,
            'type': glob.PRICETYPE.GLOBAL
        },
        glob.DAELAN: {
            'data': daelan_prices,
            'type': glob.PRICETYPE.INDIVIDUAL
        },
        glob.OB: {
            'data': ob_prices,
            'type': glob.PRICETYPE.INDIVIDUAL
        },
        glob.OLIS: {
            'data': olis_prices,
            'type': glob.PRICETYPE.GLOBAL
        },
        glob.ORKAN: {
            'data': orkan_prices,
            'type': glob.PRICETYPE.INDIVIDUAL
        },
        glob.ORKAN_X: {
            'data': orkan_prices,
            'type': glob.PRICETYPE.INDIVIDUAL
        }
    }

    list_of_stations = []
    price_keys = ['bensin95', 'bensin95_discount', 'diesel', 'diesel_discount']

    for key, station in sorted(all_stations.items()):
        station['key'] = key
        if prices_map[station['company']]['type'] == glob.PRICETYPE.INDIVIDUAL:
            for price_key in price_keys:
                if key.startswith('dn') and key not in prices_map[station['company']]['data']:
                    # <TEMPORARY DAELAN MEASURE>
                    #
                    # Daelan has received two new stations from N1 and new owners have now
                    # taken over its business, however, for now it seems they will continue
                    # to use the N1 backend to provide online fuel price on daelan.is webpage
                    # but yet these two new stations are not shown and propably won't show up
                    # until the new Daelan owners have renovated their website.
                    #
                    # Until then we tie the price on the two new stations to the price in
                    # Daelan Fellsmuli
                    #
                    # </TEMPORARY DAELAN MEASURE>
                    station[price_key] = prices_map[station['company']]['data']['dn_000'][price_key]
                else:
                    station[price_key] = prices_map[station['company']]['data'][key][price_key]
        elif prices_map[station['company']]['type'] == glob.PRICETYPE.GLOBAL:
            for price_key in price_keys:
                station[price_key] = prices_map[station['company']]['data'][price_key]
            if station['company'] == glob.N1 and key in glob.N1_PRICE_DIFF:
                # Some N1 stations have been observed in real life to have fixed
                # different prices from the most common price which is shown
                # on N1 webpage.
                for price_key in price_keys:
                    station[price_key] += glob.N1_PRICE_DIFF[key][price_key]
                # Note: hardcoded price deviances, in no way guaranteed to
                # be permanently correct.
        list_of_stations.append(station)

    data = {'stations': list_of_stations}

    data_json_pretty_file = os.path.join(current_dir, '../vaktin/gas.json')
    data_json_mini_file = os.path.join(current_dir, '../vaktin/gas.min.json')

    utils.save_to_json(data_json_pretty_file, data, pretty=True)
    utils.save_to_json(data_json_mini_file, data, pretty=False)


if __name__ == '__main__':
    main()
