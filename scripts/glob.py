#!/usr/bin/python
# -*- coding: utf-8 -*-
ATLANTSOLIA = u'Atlantsolía'
COSTCO = u'Costco Iceland'
N1 = u'N1'
DAELAN = u'Dælan'
OLIS = u'Olís'
OB = u'ÓB'
SKELJUNGUR = u'Skeljungur'
ORKAN = u'Orkan'
ORKAN_X = u'Orkan X'


class PRICETYPE:
    INDIVIDUAL = 0
    GLOBAL = 1


ATLANTSOLIA_LOCATION_RELATION = {
    u'Akureyri Baldursnes': 'ao_000',
    u'Akureyri Gler\xe1rtorg': 'ao_001',
    u'B\xedldsh\xf6f\xf0i': 'ao_002',
    u'Borgarnes': 'ao_003',
    u'B\xfa\xf0ark\xf3r': 'ao_004',
    u'Egilssta\xf0ir': 'ao_005',
    u'Hafnarfjar\xf0arh\xf6fn': 'ao_006',
    u'Hverager\xf0i': 'ao_007',
    u'Kaplakriki *': 'ao_008',
    u'K\xf3pavogsbraut': 'ao_009',
    u'Mosfellsb\xe6r': 'ao_010',
    u'Njar\xf0v\xedk': 'ao_011',
    u'\xd6skjuhl\xed\xf0': 'ao_012',
    u'Selfoss': 'ao_013',
    u'Skeifan': 'ao_014',
    u'Skemmuvegi': 'ao_015',
    u'Sk\xfalagata': 'ao_016',
    u'Sprengisandur *': 'ao_017',
    u'Stykkish\xf3lmur': 'ao_018',
    u'Starengi': 'ao_019',
    u'Kirkjust\xe9tt': 'ao_020',
    u'Knarrvogur': 'ao_021',  # typo in address?
    u'Knarravogur': 'ao_021',  # put these two just in case ..
    u'Knarrarvogur': 'ao_021',
    u'Kjalarnes': 'ao_022'
}
# Atlantsolia declared one (and now two) of its stations to be without discount,
# on their site that station is marked with a star (*) and the following comment at the bottom:
# "* Engir afslaettir gilda"
ATLANTSOLIA_DISCOUNTLESS_STATIONS = ['ao_008', 'ao_017']

OB_MINIMUM_DISCOUNT = 5
# OB has been playing the "random five stations of ours have minimum of 15 ISK discount", they
# shuffle the stations every month.
# In 2019-06 the stations are the following:
# * Baejarlind (ob_010)  <-- this station was made discountless 2019-06-04T11:39, see below
# * Thorlakshofn (ob_033)
# * Akureyri - Hlidarbraut (ob_001)
# * Blonduos (ob_007)
# * Varmahlid (ob_034)
OB_EXTRA_DISCOUNT_STATIONS = ['ob_033', 'ob_001', 'ob_007', 'ob_034']
OB_EXTRA_DISCOUNT_AMOUNT = 15
OB_EXTRA_DISCOUNT_UNTIL = '2019-06-30T23:59'
# OB joins the discountless madness
# https://www.facebook.com/ob.bensin/photos/a.208957995809394/2301004636604709/
# Says the following (2019-06-04T11:39):
# ------------------------------------------------------------------------------------------------
# OB hefur nu laekkad verð á eldsneytislitranum umtalsvert á thremur stoðvum!
# * Fjardarkaupum i Hafnarfirdi (ob_012)
# * Arnarsmara í Kopavogi (ob_003)
# * Baejarlind í Kopavogi (ob_010)
# Bensinslitrinn á thessum stodvum er nu a 211.4 ISK og disellitrinn a 202 ISK
# Afslattur med lyklum og kortum gildir ekki a thessum stodvum. Allir lykil-og korthafar Olis og
# OB njota eftir sem adur afslattar af eldsneyti og odrum vorum a Olis og OB stodvum um land allt.
# ------------------------------------------------------------------------------------------------
OB_DISCOUNTLESS_STATIONS = ['ob_012', 'ob_003', 'ob_010']

ORKAN_LOCATION_RELATION = {
    u'Dalvegur': 'or_000',
    u'Gylfafl\xf6t': 'or_001',
    u'Klettagar\xf0ar': 'or_002',
    u'K\xe6nan': 'or_003',
    u'Laugavegur': 'or_004',
    u'Miklabraut': 'or_005',
    u'Reykjav\xedkurvegur': 'or_006',
    u'Sk\xf3garhl\xed\xf0': 'or_007',
    u'Su\xf0urstr\xf6nd': 'or_008',
    u'Egilssta\xf0ir, Fagradalsbraut': 'or_009',
    u'Eskifj\xf6r\xf0ur': 'or_010',
    u'F\xe1skr\xfa\xf0sfj\xf6r\xf0ur': 'or_011',
    u'Hallormssta\xf0ur': 'or_012',
    u'Neskaupsta\xf0ur': 'or_013',
    u'Rey\xf0arfj\xf6r\xf0ur': 'or_014',
    u'Sey\xf0isfj\xf6r\xf0ur': 'or_015',
    u'Skj\xf6ld\xf3lfssta\xf0ir': 'or_016',
    u'\xc1rsk\xf3gssandur': 'or_017',
    u'Furuvellir': 'or_018',
    u'H\xfasav\xedk': 'or_019',
    u'Hvammstangi': 'or_020',
    u'M\xfdrarvegur': 'or_021',
    u'M\xfdvatn': 'or_022',
    u'Sau\xf0\xe1rkr\xf3kur': 'or_023',
    u'B\xedldudalur': 'or_024',
    u'Bolungarv\xedk': 'or_025',
    u'\xcdsafj\xf6r\xf0ur': 'or_026',
    u'S\xfa\xf0av\xedk': 'or_027',
    u'Akranes, Skagabraut': 'or_028',
    u'Borgarnes': 'or_029',
    u'Grundarfj\xf6r\xf0ur': 'or_030',
    u'Hre\xf0avatnssk\xe1li': 'or_031',
    u'H\xfasafell': 'or_032',
    u'\xd3lafsv\xedk': 'or_033',
    u'Stykkish\xf3lmur': 'or_034',
    u'Grindav\xedk': 'or_035',
    u'Keflav\xedkurflugv\xf6llur': 'or_036',
    u'Reykjanesb\xe6r': 'or_037',
    u'Sandger\xf0i': 'or_038',
    u'Freysnes': 'or_039',
    u'Hvolsv\xf6llur': 'or_040',
    u'Selfoss': 'or_041',
    u'Stokkseyri': 'or_042',
    u'\xdathl\xed\xf0': 'or_043',
    u'Vestmannaeyjar': 'or_044',
    u'V\xedk \xed M\xfdrdal': 'or_045',
    u'\xdeorl\xe1ksh\xf6fn': 'or_046',
    u'Birkimelur': 'or_047',
    u'B\xfasta\xf0avegur': 'or_048',
    u'Kleppsvegur': 'or_049',
    u'Sm\xe1rinn': 'or_050',
    u'Su\xf0urfell': 'or_051',
    u'Vesturlandsvegur': 'or_052',
    u'H\xf6rg\xe1rbraut': 'or_053',
    u'Hverager\xf0i': 'or_054',
    u'Gar\xf0ab\xe6r': 'or_055',
    u'Miklabraut v. Kringluna': 'or_056'
}

ORKAN_X_LOCATION_RELATION = {
    u'Ei\xf0istorg (Orkan X)': 'ox_000',
    u'Ei\xf0istorg': 'ox_000',
    u'Miklabraut v. Kringluna (Orkan X)': 'ox_001',
    u'Skemmuvegur (Orkan X)': 'ox_002',
    u'Skemmuvegur': 'ox_002',
    u'Sp\xf6ngin (Orkan X)': 'ox_003',
    u'Egilssta\xf0ir (Orkan X)': 'ox_004',
    u'Akureyri, Kjarnagata (Orkan X)': 'ox_005',
    u'Akranes, Smi\xf0juv\xf6llum (Orkan X)': 'ox_006',
    u'Hverager\xf0i (Orkan X)': 'ox_007',
    u'Hraunb\xe6r (Orkan X)': 'ox_009',
}

# Atlantsolía has changed their discount system to mirror Orkan, this discount
# system is called "MEIRA FYRIR ÞIG".
# https://www.atlantsolia.is/daelulykill/afslattur-og-avinningur/
# MEIRA FYRIR ÞIG discount info:
# 0-49,99L   [  5 ISK ] + [ 2 ISK on your personal station] = [  7 ISK ]
# 50-149,99L [  7 ISK ] + [ 2 ISK on your personal station] = [  9 ISK ]
# 150L       [ 10 ISK ] + [ 2 ISK on your personal station] = [ 12 ISK ]
# The default discount, available to all who have the Atlantsolía pump key, and
# regardless of station, is 5 ISK.
# Additionally they provide an extra 2 ISK discount on a single station of your
# personal choice.
# Source:
# https://www.atlantsolia.is/daelulykill/afslattur-og-avinningur/
ATLANTSOLIA_MINIMUM_DISCOUNT = 5.0

# N1 offers discount of 5 ISK and 2 N1 points per liter according to the
# following page: https://www.n1.is/n1-kortid/saekja-um-kort/
# +++
# Eldsneyti: 5 króna afsláttur af bensín og dísel og 2 N1 punktar að auki á
# á hvern lítra
# +++
# These N1 points are a type of credits at N1 which you can exchange for
# gasoline (and/or periodic offers they provide) at the rate 1 ISK per
# point, but as it's a form of earned credits which you can only use doing
# business with the N1 company and not an actual discount we disregard the
# disregard the N1 points but value the 5 ISK discount.
N1_DISCOUNT = 5.0
# Since 2018-05-17 (see commit c308d1a7b5e088ddf8ef99f3ca00aa29af39019e) we've
# observed that N1 in Storihjalli maintains 8 ISK lower fuel price there than
# elsewhere. This has since then been checked occasionally in real world and
# is correct still today. But please note, hardcoded fixed price deviances like
# this might suddenly change and there might be more price deviance stations out
# there currently or in the future.
# Planning to add a note on N1 stations shown on Gasvaktin.is stating
# something similar as "the most common self-service price", similar to the
# message shown on n1.is/thjonusta/eldsneyti/ and has been stated as far as we
# know since 2018-05-17.
# N1 Fossvogur observed to be a price deviant station IRL, was first 3 ISK lower,
# then at some point changed to 5 ISK and has held that number for I believe two
# price changes.
# N1 Isafjordur suspected of deviance, phone call and asking for the fuel price
# resulted in price deviance information shown below. Not observed price deviance
# by myself, so there is of course a possibility that employee who answered me on
# the phone provided me with incorrect price data.
N1_PRICE_DIFF = {
    'n1_005': {  # Fossvogur
        'bensin95': -6.0,
        'bensin95_discount': -6.0,
        'diesel': -6.0,
        'diesel_discount': -6.0
    },
    'n1_006': {  # Storihjalli
        'bensin95': -9.0,
        'bensin95_discount': -9.0,
        'diesel': -9.0,
        'diesel_discount': -9.0
    },
    'n1_007': {  # Laekjargata
        'bensin95': -3.0,
        'bensin95_discount': -3.0,
        'diesel': -3.0,
        'diesel_discount': -3.0
    },
    'n1_011': {  # Reykjavikurvegur
        'bensin95': -12.0,
        'bensin95_discount': -12.0,
        'diesel': -12.0,
        'diesel_discount': -12.0
    },
    'n1_017': {  # Isafjordur
        'bensin95': -3.0,
        'bensin95_discount': -3.0,
        'diesel': 0.0,
        'diesel_discount': 0.0
    }
}

# Orkan has a 3-step discount system controlled by your spendings on gas from
# them in the previous motnth
# See more info here: https://www.orkan.is/Afslattarthrep
# Discount info:
# Step 1, 0-50L,   [ 5 ISK ] + [ 2 ISK if your personal station] = [  7 ISK ]
# Step 2, 50-150L, [ 6 ISK ] + [ 2 ISK if your personal station] = [  8 ISK ]
# Step 3, 150L+,   [ 8 ISK ] + [ 2 ISK if your personal station] = [ 10 ISK ]
ORKAN_MINIMUM_DISCOUNT = 5.0

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

BAD_AUTOPRICES_CHANGES = [
    {
        'timestamp_text': '2017-04-06T09:38',
        'commit_hash': 'a0783100209f0cf43b28271e3433c2c56c650447',
        'note': 'N1 bad change (23.5 ISK up and down)'
    },
    {
        'timestamp_text': '2017-06-15T23:15',
        'commit_hash': '821ccc907fec62415cc6d57f93d953205fd4d331',
        'note': 'Dælan diesel changed for a short time to N1 price and back'
    },
    {
        'timestamp_text': '2017-07-13T08:30',
        'commit_hash': 'fbf5eb81cbca3ed2091280b6cb6746975d309616',
        'note': 'Orkan bad change (down to Orkan X like price and back up)'
    },
    {
        'timestamp_text': '2017-10-25T21:45',
        'commit_hash': 'ab4f01ccbe5486adc1ee838a892344035d4cc86b',
        'note': 'Dælan diesel changed for a short time to N1 price and back'
    },
    {
        'timestamp_text': '2017-10-27T11:30',
        'commit_hash': 'f5439ce43ae49d5926a48a9be52888d56075c8f1',
        'note': 'Dælan diesel changed for a short time to N1 price and back'
    },
    {
        'timestamp_text': '2017-10-27T16:00',
        'commit_hash': 'b050ad1a673223f5a2fe2993997041614484855f',
        'note': 'slight price log where Dælan diesel was still wrong'
    },
    {
        'timestamp_text': '2018-01-11T11:00',
        'commit_hash': '5c031c459ada0b95347da63c9e33d83954a8e609',
        'note': 'Orkan bad change (~100 ISK down and back up)'
    }
]
