#!/usr/bin/python
# -*- coding: utf-8 -*-
ATLANTSOLIA = u'Atlantsolía'
N1 = u'N1'
DAELAN = u'Dælan'
OLIS = u'Olís'
OB = u'ÓB'
SKELJUNGUR = u'Skeljungur'
ORKAN = u'Orkan'
ORKAN_X = u'Orkan X'

ATLANTSOLIA_LOCATION_RELATION = {
    u'Akureyri Baldursnes': 'ao_000',
    u'Akureyri Gler\xe1rtorg': 'ao_001',
    u'B\xedldsh\xf6f\xf0i': 'ao_002',
    u'Borgarnes': 'ao_003',
    u'B\xfa\xf0ark\xf3r': 'ao_004',
    u'Egilssta\xf0ir': 'ao_005',
    u'Hafnarfjar\xf0arh\xf6fn': 'ao_006',
    u'Hverager\xf0i': 'ao_007',
    u'Kaplakriki': 'ao_008',
    u'K\xf3pavogsbraut': 'ao_009',
    u'Mosfellsb\xe6r': 'ao_010',
    u'Njar\xf0v\xedk': 'ao_011',
    u'\xd6skjuhl\xed\xf0': 'ao_012',
    u'Selfoss': 'ao_013',
    u'Skeifan': 'ao_014',
    u'Skemmuvegi': 'ao_015',
    u'Sk\xfalagata': 'ao_016',
    u'Sprengisandur': 'ao_017',
    u'Stykkish\xf3lmur': 'ao_018'
}

ORKAN_X_LOCATION_RELATION = {
    u'Ei\xf0istorg (Orkan X)': 'ox_000',
    u'Miklabraut v. Kringluna (Orkan X)': 'ox_001',
    u'Skemmuvegur (Orkan X)': 'ox_002',
    u'Sp\xf6ngin (Orkan X)': 'ox_003',
    u'Egilssta\xf0ir (Orkan X)': 'ox_004',
    u'Akureyri, Kjarnagata (Orkan X)': 'ox_005',
    u'Akranes, Smi\xf0juv\xf6llum (Orkan X)': 'ox_006',
    u'Hverager\xf0i (Orkan X)': 'ox_007',
}

# Atlantsolía has changed their discount system to mirror Orkan
# https://www.atlantsolia.is/daelulykill/afslattur-og-avinningur/
# the default discount, available to all who have the Atlantsolía pump key, is
# 3.2 ISK
# Source:
# https://www.atlantsolia.is/daelulykill/afslattur-og-avinningur/
ATLANTSOLIA_MINIMUM_DISCOUNT = 3.0

# Orkan has a 3-step discount system controlled by your spendings on gas from
# them the month before
# See more info here: https://www.orkan.is/Afslattarthrep
# Discount info:
# Step 1, 0-50L,   [ 3 ISK ] + [ 2 ISK if your personal station] = [  5 ISK ]
# Step 2, 50-150L, [ 5 ISK ] + [ 2 ISK if your personal station] = [  7 ISK ]
# Step 3, 150L+,   [ 8 ISK ] + [ 2 ISK if your personal station] = [ 10 ISK ]
ORKAN_MINIMUM_DISCOUNT = 3.0

BROWSERS_UA = [
    ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) '
     'Chrome/17.0.963.66 Safari/535.11'),
    ('Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) '
     'Chrome/17.0.963.66 Safari/535.11'),
    ('Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like '
     'Gecko) Chrome/17.0.963.66 Safari/535.11'),
    ('Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) '
     'Chrome/17.0.963.66 Safari/535.11'),
    ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like '
     'Gecko) Chrome/17.0.963.66 Safari/535.11'),
    ('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) '
     'Chrome/17.0.963.66 Safari/535.11'),
    ('Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like '
     'Gecko) Chrome/17.0.963.66 Safari/535.11'),
    ('Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) '
     'Chrome/17.0.963.66 Safari/535.11'),
    ('Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) '
     'Chrome/17.0.963.66 Safari/535.11'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.11 '
     '(KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.11 '
     '(KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.11 '
     '(KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8) AppleWebKit/535.11 '
     '(KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11'),
    ('Mozilla/5.0 (X11; Linux amd64) AppleWebKit/535.1 (KHTML, like Gecko) '
     'Chrome/13.0.782.24 Safari/535.1'),
    ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like '
     'Gecko) Chrome/13.0.782.24 Safari/535.1'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.1 (KHTML,'
     ' like Gecko) Chrome/13.0.782.24 Safari/535.1'),
    ('Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:14.0) Gecko/20120405 '
     'Firefox/14.0a1'),
    ('Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20120405 Firefox/14.0a1'),
    ('Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20120405 Firefox/14.0a1'),
    ('Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 '
     'Firefox/16.0.1'),
    ('Mozilla/5.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 '
     'Firefox/16.0.1'),
    ('Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 '
     'Firefox/16.0.1)')
]
