#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------------------------- #
import argparse

import logman
from scripts import scraper
from scripts import pricer

__author__ = "Sveinn Floki Gudmundsson"
__email__ = "svefgud@gmail.com"
__credits__ = ["Sveinn Floki Gudmundsson"]
__maintainer__ = "Sveinn Floki Gudmundsson"
__version__ = "0.0.1"


def main(arguments):
    print(arguments)
    logman.init(role=arguments['role'])
    if 'none' not in arguments['scrape']:
        logman.info('Running scraper testrun ..')
        scraper.testrun(arguments['scrape'])
    if arguments['scrape-and-write-data']:
        logman.info('Scraping price data and writing to vaktin ..')
        pricer.main()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Gasvaktin', formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-r', '--role', default='cli', help=(
        'Define runner role.'
    ))
    parser.add_argument('-s', '--scrape', default='none', metavar=('COMPANIES', ), help=(
        'Run oil companies scraper for selected companies.\n'
        'Optional, comma separated company names (Default: "none").\n'
        'Examples: "atlantsolia,costco,daelan", "ao,co,dn,n1,ob,ol,or,ox", "all" or "none".'
    ))
    parser.add_argument('-sw', '--scrape-and-write-data', action='store_true', help=(
        'Write collected data to files in ./vaktin/ directory.'
    ))
    pargs = parser.parse_args()
    arguments = {
        'role': 'cli',
        'scrape': pargs.scrape.split(','),
        'scrape-and-write-data': pargs.scrape_and_write_data
    }
    main(arguments)
