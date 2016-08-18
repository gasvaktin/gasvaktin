#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import datetime
import json
import os
import sys

import git

DESC = 'Average-prices-over-time data extractor tool for Gasvaktin'
# Used to extract price changes over periods of time from the gasvaktin repo.


def calc_mean(my_list):
    '''
    Miðgildi (e. mean)
    '''
    sorted_list = sorted(my_list)
    return sorted_list[len(sorted_list) / 2]


def calc_median(mylist):
    '''
    Meðaltal (e. median)
    '''
    return sum(mylist) / max(len(mylist), 1)


def one_decimal(my_float):
    '''
    Rounds float to one decimal place
    '''
    return int(my_float * 10) / 10.0


def fail_nicely(parser, error_msg):
    '''
    @parser: instance of argparse.ArgumentParser()
    @error_msg: text containing error message
    '''
    parser.print_help()
    sys.stderr.write('Error: %s\n' % (error_msg, ))
    sys.exit(2)


def compare_samples(cur, prev):
    '''
    Checks if two samples hold same prices
    '''
    return (
        cur['mean_bensin95'] == prev['mean_bensin95'] and
        cur['mean_bensin95_discount'] == prev['mean_bensin95_discount'] and
        cur['median_bensin95'] == prev['median_bensin95'] and
        cur['median_bensin95_discount'] == prev['median_bensin95_discount'] and
        cur['mean_diesel'] == prev['mean_diesel'] and
        cur['mean_diesel_discount'] == prev['mean_diesel_discount'] and
        cur['median_diesel'] == prev['median_diesel'] and
        cur['median_diesel_discount'] == prev['median_diesel_discount']
    )


def read_price_changes(parser, repo, fromdate=None, todate=None):
    '''
    @repo: instance of git.Repo() for the gasvaktin repo
    @fromdate: string containing date on format YYYY-MM-DD
    @todate: string containing date on format YYYY-MM-DD
    returns a data filled object
    '''
    if fromdate is not None:
        try:
            fromdate = datetime.datetime.strptime(fromdate, '%Y-%m-%d')
        except:
            fail_nicely('--from-date not in format YYYY-MM-DD')
    if todate is not None:
        try:
            todate = datetime.datetime.strptime(fromdate, '%Y-%m-%d')
        except:
            fail_nicely('--to-date not in format YYYY-MM-DD')
    path = 'vaktin/gas.json'
    revgenerator = (  # commits generator
        (commit, (commit.tree / path).data_stream.read())
        for commit in repo.iter_commits(paths=path)
    )
    revlist = []  # consuming generator to list because want to reverse it :(
    for commit, filecontents in revgenerator:
        if not commit.message.startswith('auto.prices.update'):
            # we only need to read from auto.prices.update commits
            # so we skip all the others
            continue
        if commit.message.startswith('auto.prices.update.min'):
            # skip the 'min' auto commits
            continue
        timestamp_text = commit.message[19:35]
        timestamp = datetime.datetime.strptime(
            timestamp_text,
            '%Y-%m-%dT%H:%M'
        )
        if fromdate and timestamp < fromdate:
            # ignore price changes before from-date if provided
            continue
        if todate and todate < timestamp:
            # ignore price changes after to-date if provided
            continue
        timestamp_text = commit.message[19:35]
        stations = json.loads(filecontents)
        revlist.append((timestamp_text, stations))
    revlist = reversed(revlist)
    price_changes = {}
    for timestamp_text, stations in revlist:
        data = {}
        for station in stations['stations']:
            c_key = station['key'][:2]
            if c_key not in data:
                data[c_key] = {
                    'b': [],
                    'd': [],
                    'b_d': [],
                    'd_d': []
                }
            data[c_key]['b'].append(station['bensin95'])
            data[c_key]['d'].append(station['diesel'])
            if station['bensin95_discount'] is not None:
                data[c_key]['b_d'].append(station['bensin95_discount'])
            if station['diesel_discount'] is not None:
                data[c_key]['d_d'].append(station['diesel_discount'])
        for key in data:
            if key not in price_changes:
                price_changes[key] = []

            sample = {
                'mean_bensin95': calc_mean(data[key]['b']),
                'mean_bensin95_discount': (
                    calc_mean(data[key]['b_d']) if data[key]['b_d'] else None
                ),
                'median_bensin95': one_decimal(calc_median(data[key]['b'])),
                'median_bensin95_discount': (
                    one_decimal(calc_median(data[key]['b_d']))
                    if data[key]['b_d'] else None
                ),
                'mean_diesel': calc_mean(data[key]['d']),
                'mean_diesel_discount': (
                    one_decimal(calc_mean(data[key]['d_d']))
                    if data[key]['d_d'] else None
                ),
                'median_diesel': one_decimal(calc_median(data[key]['d'])),
                'median_diesel_discount': (
                    one_decimal(calc_median(data[key]['d_d']))
                    if data[key]['d_d'] else None
                ),
                'stations_count': len(data[key]['b']),
                'timestamp': timestamp_text,
            }
            prev = price_changes[key][-1] if price_changes[key] else None
            if not price_changes[key] or not compare_samples(sample, prev):
                price_changes[key].append(sample)
    return price_changes


def save_to_json(filepath, data, pretty=False):
    '''
    takes in filepath and data object saves data to json in filepath
    '''
    if pretty:
        data_text = json.dumps(
            data,
            indent=4,
            ensure_ascii=False,
            sort_keys=True
        )
    else:
        data_text = json.dumps(
            data,
            separators=(',', ':'),
            ensure_ascii=False,
            sort_keys=True
        )
    print >> open(filepath, 'w'), data_text

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument(  # example: '~/repo/gasvaktin'
        '-r',
        '--repository',
        help='Path to gasvaktin repository',
        required=True
    )
    parser.add_argument(
        '-f',
        '--from-date',
        help='Start date of time period to extract data',
        required=False
    )
    parser.add_argument(
        '-t',
        '--to-date',
        help='End date of time period to extract data',
        required=False
    )
    my_args = parser.parse_args()
    repo_path = my_args.repository
    if not os.path.exists(repo_path):
        fail_nicely(parser, 'Path "%s" seems to not exist.' % (repo_path, ))
    try:
        repo = git.Repo(repo_path)
    except:
        error_msg = 'Could not read git repo from "%s".' % (repo_path, )
        fail_nicely(parser, error_msg)
    price_changes = read_price_changes(
        parser,
        repo,
        fromdate=my_args.from_date,
        todate=my_args.to_date
    )
    out_name = 'price_changes'
    save_to_json('%s.json' % (out_name, ), price_changes, pretty=True)
    save_to_json('%s.min.json' % (out_name, ), price_changes)
