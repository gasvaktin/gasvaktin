#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs, json, random

import glob

def bytify(input):
	'''
	helper function to save utf-8 texts to json without the
	escape sequences
	http://stackoverflow.com/q/18337407
	'''
	if isinstance(input, dict):
		return {bytify(key): bytify(value)
			for key, value in input.iteritems()}
	elif isinstance(input, list):
		return [bytify(element) for element in input]
	elif isinstance(input, unicode):
		return input.encode('utf-8')
	elif isinstance(input, str):
		return unicode(input).encode('utf-8')
	else:
		return input

def load_json(filepath):
	'''
	takes in filepath to json file, reads it and returns a
	python object
	'''
	json_text = codecs.open(
		filepath,
		encoding='utf-8'
	).read()
	return json.loads(json_text)

def save_to_json(filepath, data, pretty=False):
	'''
	takes in filepath and data object
	saves data to json in filepath
	'''
	bytified_data = bytify(data)
	if pretty:
		data_text = json.dumps(
			bytified_data,
			indent=4,
			ensure_ascii=False,
			sort_keys=True
		)
	else:
		data_text = json.dumps(
			bytified_data,
			separators=(',', ':'),
			ensure_ascii=False,
			sort_keys=True
		)
	print >> open(filepath,'w'), data_text

def random_UA():
	return random.choice(glob.BROWSERS_UA)

def headers():
	return {'User-Agent': random_UA()}
