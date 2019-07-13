#!/usr/bin/python3
# -*- coding: utf-8 -*-
ATLANTSOLIA = 'Atlantsolía'
COSTCO = 'Costco Iceland'
N1 = 'N1'
DAELAN = 'Dælan'
OLIS = 'Olís'
OB = 'ÓB'
SKELJUNGUR = 'Skeljungur'
ORKAN = 'Orkan'
ORKAN_X = 'Orkan X'


class PRICETYPE:
    INDIVIDUAL = 0
    GLOBAL = 1


ATLANTSOLIA_LOCATION_RELATION = {
    'Akureyri Baldursnes': 'ao_000',
    'Akureyri Glerártorg': 'ao_001',
    'Bíldshöfði': 'ao_002',
    'Borgarnes': 'ao_003',
    'Búðarkór': 'ao_004',
    'Egilsstaðir': 'ao_005',
    'Hafnarfjarðarhöfn': 'ao_006',
    'Hveragerði': 'ao_007',
    'Kaplakriki *': 'ao_008',
    'Kópavogsbraut': 'ao_009',
    'Mosfellsbær': 'ao_010',
    'Njarðvík': 'ao_011',
    'Öskjuhlíð': 'ao_012',
    'Selfoss': 'ao_013',
    'Skeifan': 'ao_014',
    'Skemmuvegi': 'ao_015',
    'Skúlagata': 'ao_016',
    'Sprengisandur *': 'ao_017',
    'Stykkishólmur': 'ao_018',
    'Starengi': 'ao_019',
    'Kirkjustétt': 'ao_020',
    'Knarrvogur': 'ao_021',  # typo in address?
    'Knarravogur': 'ao_021',  # put these two just in case ..
    'Knarrarvogur': 'ao_021',
    'Kjalarnes': 'ao_022',
    'Háaleitisbraut': 'ao_023'
}
# Atlantsolia declared one (and now two) of its stations to be without discount,
# on their site that station is marked with a star (*) and the following comment at the bottom:
# "* Engir afslaettir gilda"
ATLANTSOLIA_DISCOUNTLESS_STATIONS = ['ao_008', 'ao_017']

OLIS_MINIMUM_DISCOUNT = 5
OLIS_LOCATION_RELATION = {
    'Baula': 'ol_016',
    'Borgarnes': 'ol_017',
    'Akranes, Esjubraut': 'ol_012',
    'Akranes, Umboð': 'ol_013',
    'Akureyri, bensínstöð': 'ol_014',
    'Arnarstapi - bensínstöð': 'ol_015',
    'Álfheimar': 'ol_001',
    'Ánanaust': 'ol_002',
    'Básinn': 'ol_025',
    'Dalvík Bensínstöð': 'ol_018',
    'Fellabær': 'ol_019',
    'Ferstikla Veitingaskáli': 'ol_020',
    'Garðabær': 'ol_004',
    'Gullinbrú': 'ol_005',
    'Hamraborg': 'ol_006',
    'Hella - bensínstöð': 'ol_021',
    'Hornafjörður bensínst.': 'ol_024',
    'Húsavík': 'ol_023',
    'Klöpp': 'ol_008',
    'Langitangi': 'ol_009',
    'Litla-Kaffistofan': 'ol_027',
    'Mjódd': 'ol_000',
    'Neskaupstaður': 'ol_028',
    'Norðlingaholt': 'ol_010',
    'Ólafsfjörður, bensínstöð': 'ol_029',
    'Reyðarfjörður': 'ol_030',
    'Sauðárkrókur - þjónustust.': 'ol_031',
    'Selfoss': 'ol_032',
    'Siglufjörður bensínstöð': 'ol_033',
    'Skagaströnd bensínst.': 'ol_034',
    'Sæbraut': 'ol_011'
}
OB_MINIMUM_DISCOUNT = 5
OB_LOCATION_RELATION = {
    'Arnarsmára': 'ob_003',
    'Bæjarlind': 'ob_010',
    'Fjarðarkaup': 'ob_012',
    'Borgarnes': 'ob_009',
    'Akranes, Esjubraut': 'ob_000',
    'Aðalgötu': 'ob_035',
    'Akureyri': 'ob_001',
    'Akureyri BSÓ': 'ob_002',
    'Barðastaðir': 'ob_004',
    'Baula': 'ob_005',
    'Bíldshöfða': 'ob_006',
    'Blönduós': 'ob_007',
    'Bolungarvík': 'ob_008',
    'Búðardalur': '',  # note: station missing
    'Eyrarbakka': 'ob_011',
    'Grindavík': 'ob_014',
    'Grundartanga': 'ob_015',
    'Hólmavík': 'ob_016',
    'Húsavík': 'ob_017',
    'Ísafjörður': 'ob_018',
    'Kirkjubæjarklaustur': 'ob_019',
    'Landvegamót': 'ob_020',
    'Laugabakki': 'ol_036',
    'Melabraut': 'ob_021',
    'Minni Borg': 'ob_022',
    'Neskaupstaður': 'ob_023',
    'Njarðvík': 'ob_024',
    'Reyðarfjörður': 'ob_026',
    'Selfoss': 'ob_027',
    'Snorrabraut': 'ob_028',
    'Stykkishólmur': 'ob_030',
    'Suðurhella': 'ob_031',
    'Varmahlíð': 'ob_034',
    'Vestmannaeyjar Klettur': 'ob_032',
    'Þorlákshöfn': 'ob_033'
}
# OB has been playing the "random five stations of ours have minimum of 15 ISK discount", they
# shuffle the stations every month.
# In 2019-07 the stations are the following:
# https://www.facebook.com/ob.bensin/photos/a.208957995809394/2349874545051051/
# * Stykkishólmur
# * Bolungarvík
# * Reyðarfjörður
# * Selfoss
# * Njarðvík
OB_EXTRA_DISCOUNT_STATIONS = ['ob_030', 'ob_008', 'ob_026', 'ob_027', 'ob_024']
OB_EXTRA_DISCOUNT_AMOUNT = 15
OB_EXTRA_DISCOUNT_UNTIL = '2019-07-31T23:59'
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
    'Dalvegur': 'or_000',
    'Gylfaflöt': 'or_001',
    'Klettagarðar': 'or_002',
    'Kænan': 'or_003',
    'Laugavegur': 'or_004',
    'Miklabraut': 'or_005',
    'Reykjavíkurvegur': 'or_006',
    'Skógarhlíð': 'or_007',
    'Suðurströnd': 'or_008',
    'Egilsstaðir, Fagradalsbraut': 'or_009',
    'Eskifjörður': 'or_010',
    'Fáskrúðsfjörður': 'or_011',
    'Hallormsstaður': 'or_012',
    'Neskaupstaður': 'or_013',
    'Reyðarfjörður': 'or_014',
    'Seyðisfjörður': 'or_015',
    'Skjöldólfsstaðir': 'or_016',
    'Árskógssandur': 'or_017',
    'Furuvellir': 'or_018',
    'Húsavík': 'or_019',
    'Hvammstangi': 'or_020',
    'Mýrarvegur': 'or_021',
    'Mývatn': 'or_022',
    'Sauðárkrókur': 'or_023',
    'Bíldudalur': 'or_024',
    'Bolungarvík': 'or_025',
    'Ísafjörður': 'or_026',
    'Súðavík': 'or_027',
    'Akranes, Skagabraut': 'or_028',
    'Borgarnes': 'or_029',
    'Grundarfjörður': 'or_030',
    'Hreðavatnsskáli': 'or_031',
    'Húsafell': 'or_032',
    'Ólafsvík': 'or_033',
    'Stykkishólmur': 'or_034',
    'Grindavík': 'or_035',
    'Keflavíkurflugvöllur': 'or_036',
    'Reykjanesbær': 'or_037',
    'Sandgerði': 'or_038',
    'Freysnes': 'or_039',
    'Hvolsvöllur': 'or_040',
    'Selfoss': 'or_041',
    'Stokkseyri': 'or_042',
    'Úthlíð': 'or_043',
    'Vestmannaeyjar': 'or_044',
    'Vík í Mýrdal': 'or_045',
    'Þorlákshöfn': 'or_046',
    'Birkimelur': 'or_047',
    'Bústaðavegur': 'or_048',
    'Kleppsvegur': 'or_049',
    'Smárinn': 'or_050',
    'Suðurfell': 'or_051',
    'Vesturlandsvegur': 'or_052',
    'Hörgárbraut': 'or_053',
    'Hveragerði': 'or_054',
    'Garðabær': 'or_055',
    'Miklabraut v. Kringluna': 'or_056'
}

ORKAN_X_LOCATION_RELATION = {
    u'Eiðistorg (Orkan X)': 'ox_000',
    u'Eiðistorg': 'ox_000',
    u'Miklabraut v. Kringluna (Orkan X)': 'ox_001',
    u'Skemmuvegur (Orkan X)': 'ox_002',
    u'Skemmuvegur': 'ox_002',
    u'Spöngin (Orkan X)': 'ox_003',
    u'Spöngin': 'ox_003',
    u'Egilsstaðir (Orkan X)': 'ox_004',
    u'Akureyri, Kjarnagata (Orkan X)': 'ox_005',
    u'Akranes, Smiðjuvöllum (Orkan X)': 'ox_006',
    u'Hveragerði (Orkan X)': 'ox_007',
    u'Hraunbær (Orkan X)': 'ox_009',
}
ORKAN_DISCOUNTLESS_STATIONS = ['or_000', 'or_006']

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
    'n1_013': {  # Borgarnes
        'bensin95': -6.0,
        'bensin95_discount': -6.0,
        'diesel': -6.0,
        'diesel_discount': -6.0
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
