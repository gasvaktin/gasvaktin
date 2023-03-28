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


def headers(bot=False):
    '''
    get headers object with random user agent
    '''
    # Why wear a mask?
    #
    # One reason for wearing a mask is to pretend to be someone or something else. The mask can be
    # a kind of language that expresses the emotion of the figure one chooses to create. When one
    # sees a person wearing a mask depicting a happy expression, what do you think it means? It may
    # infer several meanings. It may convey the mask wearer's genuine happiness to other people,
    # and make them laugh, or it may mask, or hide, the wearer's real emotions, such as
    # unhappiness. Some mask may serve more than one purpose.
    return {'User-Agent': random_ua() if bot is False else globs.BOT_UA}
