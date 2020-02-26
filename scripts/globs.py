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
    'Skemmuvegur': 'ao_015',
    'Skúlagata': 'ao_016',
    'Sprengisandur *': 'ao_017',
    'Stykkishólmur': 'ao_018',
    'Starengi': 'ao_019',
    'Kirkjustétt': 'ao_020',
    'Knarrvogur': 'ao_021',  # typo in address?
    'Knarravogur': 'ao_021',  # put these two just in case ..
    'Knarrarvogur': 'ao_021',
    'Kjalarnes': 'ao_022',
    'Háaleitisbraut': 'ao_023',
    'Stapabraut': 'ao_024',
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
    'Þorlákshöfn': 'ob_033',
    'Vík': 'ob_037',
    'Vík í Mýrdal': 'ob_037',
}
# OB has been playing the "random five stations of ours have minimum of 15 ISK discount", they
# shuffle the stations every month.
# In 2020-02 the stations are the following:
# https://www.facebook.com/ob.bensin/photos/a.208957995809394/2789036497801518/
# * ÓB Varmahlíð (ob_034)
# * ÓB Vestmannaeyjum (ob_032)
# * ÓB Blönduósi (ob_007)
# * ÓB Neskaupsstað (ob_023)
# * ÓB Ísafirði (ob_018)
OB_EXTRA_DISCOUNT_STATIONS = ['ob_034', 'ob_032', 'ob_007', 'ob_023', 'ob_018']
OB_EXTRA_DISCOUNT_AMOUNT = 15
OB_EXTRA_DISCOUNT_UNTIL = '2020-02-29T23:59'
# ------------------------------------------------------------------------------------------------
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
    'Miklabraut v. Kringluna': 'or_056',
    'Eiðistorg': 'or_057',
    'Skemmuvegur': 'or_058',
    'Spöngin': 'or_059',
    'Egilsstaðir, Miðvangi': 'or_060',
    'Akureyri, Kjarnagata': 'or_061',
    'Kjarnagata, Akureyri': 'or_061',
    'Akranes, Smiðjuvöllum': 'or_062',
    'Hveragerði, Sunnumörk': 'or_063',
    'Hraunbær': 'or_064'
}
ORKAN_DISCOUNTLESS_STATIONS = ['or_000', 'or_006']
# Orkan has a 3-step discount system controlled by your spendings on gas from
# them in the previous motnth
# See more info here: https://www.orkan.is/Afslattarthrep
# Discount info:
# Step 1, 0-50L,   [ 5 ISK ] + [ 2 ISK if your personal station] = [  7 ISK ]
# Step 2, 50-150L, [ 6 ISK ] + [ 2 ISK if your personal station] = [  8 ISK ]
# Step 3, 150L+,   [ 8 ISK ] + [ 2 ISK if your personal station] = [ 10 ISK ]
ORKAN_MINIMUM_DISCOUNT = 5.0

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

# N1 offers discount of 5 ISK and 2 N1 points per liter according to the following page:
# https://www.n1.is/n1-kortid/saekja-um-kortid/
# -----------------------------------------------------------------------------------------------
# N1 kortið og N1 lykillinn kosta ekkert en færa þér bæði afslátt og punkta sem gilda sem inneign
# í öllum viðskiptum við N1
# - 5 kr + 2 punktar að auki
# -16 kr + 2 punktar á afmælisdaginn þinn
# -15 kr + 2 punktar í 10. hvert skipti þegar keyptir eru 25 L eða meira af eldsneyti
# -----------------------------------------------------------------------------------------------
# These N1 points mentioned above are a type of credits at N1 which you can exchange for gasoline
# (and/or periodic offers they provide) at the rate 1 ISK per point, but as it's a form of earned
# credits which you can only use doing business with the N1 company and not an actual discount we
# disregard the N1 points but value the 5 ISK discount.
N1_DISCOUNT = 5.0
N1_LOCATION_RELATION = {
    'Ártúnshöfði': 'n1_000',
    'Bíldshöfði': 'n1_001',
    'Gagnvegur': 'n1_002',
    'Háholt': 'n1_003',
    'Borgartún': 'n1_004',
    'Fossvogur': 'n1_005',
    'Stórihjalli': 'n1_006',
    'Lækjargata': 'n1_007',
    'Hringbraut': 'n1_008',
    'Stóragerði': 'n1_009',
    'Skógarsel': 'n1_010',
    'Reykjavíkurvegur': 'n1_011',
    'Akranes': 'n1_012',
    'Borgarnes': 'n1_013',
    'Staðarskáli': 'n1_014',
    'Blönduós': 'n1_015',
    'Sauðárkrókur': 'n1_016',
    'Ísafirði': 'n1_017',
    'Akureyri Hörgárbraut': 'n1_018',
    'Akureyri Leiruvegur': 'n1_019',
    'Húsavík': 'n1_020',
    'Egilsstaðir': 'n1_021',
    'Höfn': 'n1_022',
    'Hvolsvöllur': 'n1_023',
    'Selfoss': 'n1_024',
    'Hveragerði': 'n1_025',
    'Reykjanesbær': 'n1_026',
    'Ásvellir': 'n1_027',
    'Eskifjörður': 'n1_028',
    'Reykholt': 'n1_029',
    'Breiðablik': 'n1_030',
    'Hellissandur': 'n1_031',
    'Grundarfjörður': 'n1_032',
    'Búðardalur': 'n1_033',
    'Bjarkalundur': 'n1_034',
    'Reykhólar': 'n1_035',
    'Patreksfjörður': 'n1_036',
    'Tálknafjörður': 'n1_037',
    'Þingeyri': 'n1_038',
    'Flateyri': 'n1_039',
    'Norðurfjörður': 'n1_040',
    'Drangsnes': 'n1_041',
    'Hólmavík': 'n1_042',
    'Hofsós': 'n1_043',
    'Grenivík': 'n1_044',
    'Reykjahlíð': 'n1_045',
    'Fosshóll': 'n1_046',
    'Laugar': 'n1_047',
    'Kópasker': 'n1_048',
    'Ásbyrgi': 'n1_049',
    'Raufarhöfn': 'n1_050',
    'Þórshöfn': 'n1_051',
    'Bakkafjörður': 'n1_052',
    'Dalvík': 'n1_053',
    'Vopnafjörður': 'n1_054',
    'Borgarfjörður Eystri': 'n1_055',
    'Stöðvarfjörður': 'n1_056',
    'Breiðdalsvík': 'n1_057',
    'Djúpivogur': 'n1_058',
    'Nesjar': 'n1_059',
    'Fagurhólsmýri': 'n1_060',
    'Kirkjubæjarklaustur': 'n1_061',
    'Vík': 'n1_062',
    'Vestmannaeyjar': 'n1_063',
    'Árnes': 'n1_064',
    'Flúðir': 'n1_065',
    'Geysir': 'n1_066',
    'Brautarhóll': 'n1_067',
    'Laugarvatn': 'n1_068',
    'Grindavík': 'n1_069',
    'Sandgerði': 'n1_070',
    'Garður': 'n1_071',
    'Vogar': 'n1_072',
    'Reyðarfjörður': 'n1_073',
    'Akureyri Tryggvabraut': 'n1_074',
    'Ólafsvík': 'n1_075',
    'Flókalundur': 'n1_076',
    'Ægisíða': 'n1_077',
    'Knútstöð Keflavíkurflugvelli': 'n1_078',
    'Norðlingaholt': 'n1_079',
    'Víðihlíð': 'n1_080',
    'Lindir': 'n1_081',
}
N1_DISCOUNTLESS_STATIONS = ['n1_081']

DAELAN_LOCATION_RELATION = {
    'Hæðasmári': 'dn_002',
    'Salavegur': 'dn_003',
    'Stekkjarbakki, Mjódd': 'dn_001',
    'Holtagarðar': 'dn_004',
    'Fellsmúli': 'dn_000'
}

BROWSERS_UA = [
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/74.0.3729.169 Safari/537.36'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/78.0.3904.97 Safari/537.36'),
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/77.0.3865.120 Safari/537.36'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/78.0.3904.87 Safari/537.36'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/78.0.3904.70 Safari/537.36'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko)'
     ' Version/13.0.3 Safari/605.1.15'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/78.0.3904.108 Safari/537.36'),
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko)'
     ' Version/13.0.2 Safari/605.1.15'),
    ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/78.0.3904.97 Safari/537.36'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/78.0.3904.70 Safari/537.36'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/78.0.3904.97 Safari/537.36'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/78.0.3904.97 Safari/537.36'),
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/78.0.3904.87 Safari/537.36'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/77.0.3865.90 Safari/537.36'),
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/77.0.3865.120 Safari/537.36'),
    'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0',
    ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/77.0.3865.120 Safari/537.36'),
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/78.0.3904.87 Safari/537.36'),
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
     ' Chrome/76.0.3809.100 Safari/537.36'),
    ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97'
     ' Safari/537.36')
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
