#!/usr/bin/python3
# -*- coding: utf-8 -*-
import codecs
import json
import random

try:
    from scripts import globs
except ModuleNotFoundError:
    import globs


def load_json(filepath):
    '''
    takes in filepath to json file, reads it and returns a python object
    '''
    json_text = codecs.open(filepath, encoding='utf-8').read()
    return json.loads(json_text)


def save_to_json(filepath, data, pretty=False):
    '''
    takes in filepath and data object saves data to json in filepath
    '''
    if pretty:
        data_text = json.dumps(data, indent=4, ensure_ascii=False, sort_keys=True)
    else:
        data_text = json.dumps(data, separators=(',', ':'), ensure_ascii=False, sort_keys=True)
    with open(filepath, mode='w', encoding='utf-8') as json_file:
        json_file.write(data_text)


def random_ua():
    '''
    get random user agent string
    '''
    return random.choice(globs.BROWSERS_UA)


def headers():
    '''
    get headers object with random user agent
    '''
    return {'User-Agent': random_ua()}
