#!/usr/bin/python
# -*- coding: utf-8 -*-

ATLANTSOLIA = u'Atlantsolía'
N1          = u'N1'
DAELAN      = u'Dælan'
OLIS        = u'Olís'
OB          = u'ÓB'
SKELJUNGUR  = u'Skeljungur'
ORKAN       = u'Orkan'
ORKAN_X     = u'Orkan X'

ATLANTSOLIA_LOCATION_RELATION = {
	u'Akureyri - Baldursnes':                         'ao_000',
	u'Akureyri - Gler\xe1rtorg':                      'ao_001',
	u'Reykjav\xedk - B\xedldsh\xf6f\xf0i':            'ao_002',
	u'Borgarnes':                                     'ao_003',
	u'K\xf3pavogur - B\xfa\xf0ark\xf3r':              'ao_004',
	u'Egilssta\xf0ir':                                'ao_005',
	u'Hafnarfj\xf6r\xf0ur - Hafnarfjar\xf0arh\xf6fn': 'ao_006',
	u'Hverager\xf0i':                                 'ao_007',
	u'Hafnarfj\xf6r\xf0ur - Flatahraun':              'ao_008',
	u'K\xf3pavogur - K\xf3pavogsbraut':               'ao_009',
	u'Mosfellsb\xe6r':                                'ao_010',
	u'Njar\xf0v\xedk':                                'ao_011',
	u'Reykjav\xedk - \xd6skjuhl\xed\xf0':             'ao_012',
	u'Selfoss':                                       'ao_013',
	u'Reykjav\xedk - Skeifan':                        'ao_014',
	u'K\xf3pavogur Skemmuvegur':                      'ao_015',
	u'Reykjav\xedk - Sk\xfalagata':                   'ao_016',
	u'Reykjav\xedk - Sprengisandur':                  'ao_017',
	u'Stykkish\xf3lmur':                              'ao_018'
}

ORKAN_X_LOCATION_RELATION = {
	u'Ei\xf0istorg (Orkan X)':        'ox_000',
	u'Miklabraut (vi\xf0 Kringluna)': 'ox_001',
	u'Skemmuvegur (Orkan X)':         'ox_002',
	u'Sp\xf6ngin (Orkan X)':          'ox_003',
	u'Egilssta\xf0ir':                'ox_004',
	u'Akureyri, Kjarnagata':          'ox_005',
	u'Akranes, Smi\xf0juv\xf6llum':   'ox_006',
	u'Hverager\xf0i':                 'ox_007',
}

# Atlantsolía has changed their discount system to mirror Orkan
# https://www.atlantsolia.is/daelulykill/afslattur-og-avinningur/
# the default discount, available to all who have the Atlantsolía pump key, is 3.2 ISK
# Source:
# https://www.atlantsolia.is/daelulykill/afslattur-og-avinningur/
ATLANTSOLIA_MINIMUM_DISCOUNT = 3.2

# Orkan has a 3-step discount system controlled by your spendings on gas from them the month before
# See more info here: https://www.orkan.is/Afslattarthrep
ORKAN_MINIMUM_DISCOUNT = 5.0

BROWSERS_UA = [
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
	'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
	'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
	'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
	'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
	'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
	'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
	'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
	'Mozilla/5.0 (X11; Linux amd64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:14.0) Gecko/20120405 Firefox/14.0a1',
	'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20120405 Firefox/14.0a1',
	'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20120405 Firefox/14.0a1',
	'Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
	'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
	'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1'
]
