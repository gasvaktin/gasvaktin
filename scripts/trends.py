#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import datetime
import json
import os
import sys

import git

try:
    from scripts import globs
    from scripts import utils
except ModuleNotFoundError:
    import globs
    import utils

DESC = 'Average-prices-over-time trends data extractor tool'
# Used to extract price changes over periods of time from gasvaktin repo.


def calc_median(my_list):
    '''
    Miðgildi (e. median)
    '''
    sorted_list = sorted(my_list)
    return sorted_list[int(len(sorted_list) / 2)]


def calc_mean(mylist):
    '''
    Meðaltal (e. mean)
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


def read_price_changes(repo, fromdate=None, todate=None):
    '''
    @repo: instance of git.Repo() for the gasvaktin repo
    @fromdate: string containing date on format YYYY-MM-DD
    @todate: string containing date on format YYYY-MM-DD
    returns a data filled object
    '''
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
        # skip bad price changes
        bad_commit = False
        for bad_change in globs.BAD_AUTOPRICES_CHANGES:
            if (timestamp_text == bad_change['timestamp_text'] and
                    commit.hexsha == bad_change['commit_hash']):
                bad_commit = True
                break
        if bad_commit:
            continue
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
        stations = json.loads(filecontents)
        revlist.append((timestamp_text, stations))
    revlist = reversed(revlist)
    price_changes = {}
    # add Costco trends before we started showing them
    price_changes['co'] = [
        {
            "mean_bensin95": 169.9,
            "mean_bensin95_discount": None,
            "mean_diesel": 164.9,
            "mean_diesel_discount": None,
            "median_bensin95": 169.9,
            "median_bensin95_discount": None,
            "median_diesel": 164.9,
            "median_diesel_discount": None,
            "stations_count": 3,
            "timestamp": "2017-05-19T08:00"
        },
        {
            "mean_bensin95": 169.9,
            "mean_bensin95_discount": None,
            "mean_diesel": 161.9,
            "mean_diesel_discount": None,
            "median_bensin95": 169.9,
            "median_bensin95_discount": None,
            "median_diesel": 161.9,
            "median_diesel_discount": None,
            "stations_count": 3,
            "timestamp": "2017-05-25T10:00"
        }
    ]
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
            bensin95 = station['bensin95']
            bensin95_discount = station['bensin95_discount']
            diesel = station['diesel']
            diesel_discount = station['diesel_discount']
            if c_key == 'n1' and timestamp_text < '2016-09-27T23:45':
                # We were logging wrong price for N1 up until this moment,
                # see the following commit for more info:
                # 900f702908ddcce7b9816ce4049be50eec9f8ce6
                bensin95 = station['bensin95_discount']
                bensin95_discount = bensin95 - 3
                diesel = station['diesel_discount']
                diesel_discount = diesel - 3
            data[c_key]['b'].append(bensin95)
            data[c_key]['d'].append(diesel)
            if bensin95_discount is not None:
                data[c_key]['b_d'].append(bensin95_discount)
            if diesel_discount is not None:
                data[c_key]['d_d'].append(diesel_discount)
        for key in data:
            if key not in price_changes:
                price_changes[key] = []
            mean_bensin95 = one_decimal(calc_mean(data[key]['b']))
            mean_bensin95_discount = (
                one_decimal(calc_mean(data[key]['b_d']))
                if data[key]['b_d'] else None
            )
            median_bensin95 = one_decimal(calc_median(data[key]['b']))
            median_bensin95_discount = (
                one_decimal(calc_median(data[key]['b_d']))
                if data[key]['b_d'] else None
            )
            mean_diesel = one_decimal(calc_mean(data[key]['d']))
            mean_diesel_discount = (
                one_decimal(calc_mean(data[key]['d_d']))
                if data[key]['d_d'] else None
            )
            median_diesel = one_decimal(calc_median(data[key]['d']))
            median_diesel_discount = (
                one_decimal(calc_median(data[key]['d_d']))
                if data[key]['d_d'] else None
            )
            sample = {
                'mean_bensin95': mean_bensin95,
                'mean_bensin95_discount': mean_bensin95_discount,
                'median_bensin95': median_bensin95,
                'median_bensin95_discount': median_bensin95_discount,
                'mean_diesel': mean_diesel,
                'mean_diesel_discount': mean_diesel_discount,
                'median_diesel': median_diesel,
                'median_diesel_discount': median_diesel_discount,
                'stations_count': len(data[key]['b']),
                'timestamp': timestamp_text,
            }
            prev = price_changes[key][-1] if price_changes[key] else None
            if not price_changes[key] or not compare_samples(sample, prev):
                price_changes[key].append(sample)
    # add final trend change for Skeljungur to signify they've all been
    # rebranded to Orkan
    price_changes['sk'].append({
        'mean_bensin95': None,
        'mean_bensin95_discount': None,
        'mean_diesel': None,
        'mean_diesel_discount': None,
        'median_bensin95': None,
        'median_bensin95_discount': None,
        'median_diesel': None,
        'median_diesel_discount': None,
        'stations_count': 0,
        'timestamp': "2018-02-21T15:30"
    })
    # Same for Orkan X
    price_changes['ox'].append({
        'mean_bensin95': None,
        'mean_bensin95_discount': None,
        'mean_diesel': None,
        'mean_diesel_discount': None,
        'median_bensin95': None,
        'median_bensin95_discount': None,
        'median_diesel': None,
        'median_diesel_discount': None,
        'stations_count': 0,
        'timestamp': "2020-01-25T09:00"
    })
    return price_changes


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parser = argparse.ArgumentParser(description=DESC)
    parser.add_argument(  # example: '~/repo/gasvaktin'
        '-r',
        '--repository',
        help='Path to gasvaktin repository',
        required=False
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
    parser.add_argument(
        '-o',
        '--output-directory',
        help='Output directory to write trends json files',
        required=False
    )
    my_args = parser.parse_args()
    if my_args.repository is None:
        repo_path = os.path.join(current_dir, '..')
    else:
        repo_path = my_args.repository
    if not os.path.exists(repo_path):
        fail_nicely(parser, 'Path "%s" seems to not exist.' % (repo_path, ))
    try:
        repo = git.Repo(repo_path)
    except Exception:
        error_msg = 'Could not read git repo from "%s".' % (repo_path, )
        fail_nicely(parser, error_msg)
    if my_args.from_date is not None:
        try:
            datetime.datetime.strptime(my_args.from_date, '%Y-%m-%d')
        except ValueError:
            fail_nicely(parser, '--from-date not in format YYYY-MM-DD')
    if my_args.to_date is not None:
        try:
            datetime.datetime.strptime(my_args.to_date, '%Y-%m-%d')
        except ValueError:
            fail_nicely(parser, '--to-date not in format YYYY-MM-DD')
    price_changes = read_price_changes(
        repo,
        fromdate=my_args.from_date,
        todate=my_args.to_date
    )
    if my_args.output_directory is None:
        output_directory = os.path.join(current_dir, '../vaktin/')
    else:
        output_directory = my_args.output_directory
    data_json_pretty_file = os.path.join(
        output_directory, 'trends.json'
    )
    data_json_mini_file = os.path.join(
        output_directory, 'trends.min.json'
    )
    utils.save_to_json(data_json_pretty_file, price_changes, pretty=True)
    utils.save_to_json(data_json_mini_file, price_changes, pretty=False)
