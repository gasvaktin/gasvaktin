#!/usr/bin/python3
ATLANTSOLIA = 'Atlantsolía'
COSTCO = 'Costco Iceland'
N1 = 'N1'
OLIS = 'Olís'
OB = 'ÓB'
SKELJUNGUR = 'Skeljungur'
ORKAN = 'Orkan'


class PRICETYPE:
    INDIVIDUAL = 0
    GLOBAL = 1


ATLANTSOLIA_LOCATION_RELATION = {
    'Akureyri Baldursnes': 'ao_000',
    'Akureyri Baldursnes': 'ao_000',
    'Akureyri Glerártorg': 'ao_001',
    'Bíldshöfði': 'ao_002',
    'Borgarnes': 'ao_003',
    'Búðarkór': 'ao_004',
    'Egilsstaðir': 'ao_005',
    'Hafnarfjarðarhöfn': 'ao_006',
    'Hveragerði': 'ao_007',
    'Kaplakriki': 'ao_008',
    'Kópavogsbraut': 'ao_009',
    'Mosfellsbær': 'ao_010',
    'Njarðvík': 'ao_011',
    'Öskjuhlíð': 'ao_012',
    'Öskjuhlíð': 'ao_012',
    'Selfoss': 'ao_013',
    'Selfoss': 'ao_013',
    'Skeifan': 'ao_014',
    'Skemmuvegi': 'ao_015',
    'Skemmuvegur': 'ao_015',
    'Skúlagata': 'ao_016',
    'Sprengisandur': 'ao_017',
    'Stykkishólmur': 'ao_018',
    'Starengi': 'ao_019',
    'Kirkjustétt': 'ao_020',
    'Knarrarvogur': 'ao_021',
    'Kjalarnes': 'ao_022',
    'Háaleiti': 'ao_023',
    'Stapabraut': 'ao_024',
}
# Atlantsolia declared one (then two, and now three) of its stations to be without discount,
# on their site that station is marked with a star (*) and the following comment at the bottom:
# "* Engir afslaettir gilda"
ATLANTSOLIA_DISCOUNTLESS_STATIONS = [
    'ao_000', 'ao_001', 'ao_003', 'ao_004', 'ao_008', 'ao_009', 'ao_012', 'ao_013', 'ao_016',
    'ao_017',
]

# https://www.olis.is/vinahopur
OLIS_MINIMUM_DISCOUNT = 10
OLIS_LOCATION_RELATION = {
    'Borgarnes': 'ol_017',
    'Akureyri': 'ol_014',
    'Akranes Esjubraut': 'ol_012',
    'Álfheimar': 'ol_001',
    'Ánanaust': 'ol_002',
    'Garðabær': 'ol_004',
    'Gullinbrú': 'ol_005',
    'Hella': 'ol_021',
    'Hornafjörður': 'ol_024',
    'Húsavík': 'ol_023',
    'Langitangi': 'ol_009',
    'Mjódd': 'ol_000',
    'Neskaupstaður': 'ol_028',
    'Norðlingaholt': 'ol_010',
    'Reyðarfjörður': 'ol_030',
    'Selfoss': 'ol_032',
    'Siglufjörður': 'ol_033',
    'Sæbraut': 'ol_011',
    'Hrauneyjar': 'ol_022',
}
OB_MINIMUM_DISCOUNT = 10
OB_LOCATION_RELATION = {
    'Akranes Esjubraut': 'ob_000',
    'Esjubraut': 'ob_000',
    'Akureyri Hlíðarbraut': 'ob_001',
    'Hlíðarbraut Aku (lægsta verð ÓB, engir afslættir gilda)': 'ob_001',
    'Akureyri Hlíðarbraut (lægsta verð ÓB, engir afslættir gilda)': 'ob_001',
    'Akureyri': 'ob_001',
    'BSÓ Aku': 'ob_002',
    'Akureyri BSÓ': 'ob_002',
    'Arnarsmári': 'ob_003',
    'Arnarsmára': 'ob_003',
    'Arnarsmára (lægsta verð ÓB, engir afslættir gilda)': 'ob_003',
    'Barðastaðir': 'ob_004',
    'Bæjarlind': 'ob_010',
    'Bæjarlind (lægsta verð ÓB, engir afslættir gilda)': 'ob_010',
    'Fjarðarkaup': 'ob_012',
    'Fjarðarkaup (lægsta verð ÓB, engir afslættir gilda)': 'ob_012',
    'Borgarnes': 'ob_009',
    'Borgarnes (lægsta verð ÓB, engir afslættir gilda)': 'ob_009',
    'Aðalgötu 60': 'ob_035',
    'Keflavíkurflugvöllur': 'ob_035',
    'Bíldshöfða': 'ob_006',
    'Blönduós': 'ob_007',
    'Bolungarvík': 'ob_008',
    'Eyrarbakki': 'ob_011',
    'Grindavík': 'ob_014',
    'Grundartanga': 'ob_015',
    'Grundartangi': 'ob_015',
    'Hólmavík': 'ob_016',
    'Húsavík': 'ob_017',
    'Ísafjörður': 'ob_018',
    'Kirkjubæjarklaustur': 'ob_019',
    'Landvegamót': 'ob_020',
    'Laugabakki': 'ob_036',
    'Laugarbakki': 'ob_036',
    'Melabraut': 'ob_021',
    'Minni Borg': 'ob_022',
    'Neskaupstaður': 'ob_023',
    'Njarðvík': 'ob_024',
    'Reyðarfjörður': 'ob_026',
    'Selfoss': 'ob_027',
    'Selfossi (lægsta verð ÓB, engir afslættir gilda)': 'ob_027',
    'Selfoss (lægsta verð ÓB, engir afslættir gilda)': 'ob_027',
    'Stykkishólmur': 'ob_030',
    'Suðurhella': 'ob_031',
    'Varmahlíð': 'ob_034',
    'Klettur, Vestm.eyjum': 'ob_032',
    'Vestmannaeyjum': 'ob_032',
    'Þorlákshöfn': 'ob_033',
    'Vík': 'ob_037',
    'Sjafnargötu, Aku': 'ob_038',
    'Sjafnargötu, Akureyri': 'ob_038',
    'Sauðárkókur': 'ob_039',
    'Sauðárkrókur': 'ob_039',
    'Sauðárkókur': 'ob_039',
    'Sauðárkrókur': 'ob_039',
    'Hamraborg': 'ob_040',
    'Hamraborg (lægsta verð ÓB, engir afslættir gilda)': 'ob_040',
    'Ferstikla': 'ob_041',
    'Klöpp': 'ob_042',
    'Klöpp (lægsta verð ÓB, engir afslættir gilda)': 'ob_042',
    'Ólafsfjörður': 'ob_044',
    'Skagaströnd': 'ob_045',
    'Akranes Suðurgötu': 'ob_046',
    'Fellabær': 'ob_047',
    'Arnarstapa': 'ob_078',
    'Arnarstapi': 'ob_078',
    'Básinn': 'ob_079',
    'Keflavík': 'ob_079',
    'Dalvík': 'ob_080',
    'ÓB Dalvík': 'ob_080',
    'Kjarnagata': 'ob_081',
    'Búðardalur': 'ob_082',
}
# OB has been playing the "random five stations of ours have minimum of 15 ISK discount", they
# shuffle the stations every month.
# In 2025-06 the stations are the following:
# https://www.ob.is
# * ÓB Húsavík (ob_017)
# * ÓB Vestmannaeyjum (ob_032)
# * ÓB Skagaströnd (ob_045)
# * ÓB Kirkjubæjarklaustur (ob_019)
# * ÓB Neskaupstaður (ob_023)
OB_EXTRA_DISCOUNT_STATIONS = ['ob_017', 'ob_032', 'ob_045', 'ob_019', 'ob_023']
OB_EXTRA_DISCOUNT_AMOUNT = 15
OB_EXTRA_DISCOUNT_UNTIL = '2025-06-30T23:59'
# OB discountless stations
OB_DISCOUNTLESS_STATIONS = [
    'ob_001', 'ob_003', 'ob_009', 'ob_010', 'ob_012', 'ob_027', 'ob_036', 'ob_040', 'ob_042'
]

ORKAN_LOCATION_RELATION = {
    'Dalvegur': 'or_000',
    'Gylfaflöt': 'or_001',
    'Klettagarðar': 'or_002',
    'Klettagörðum': 'or_002',
    'Kænan': 'or_003',
    'Kænunni': 'or_003',
    'Laugavegur': 'or_004',
    'Laugavegi': 'or_004',
    'Miklabraut': 'or_005',
    'Miklabraut Norður': 'or_005',
    'Miklubraut N': 'or_005',
    'Miklabraut við Lyfjaval': 'or_005',
    'Reykjavíkurvegur': 'or_006',
    'Hafnarfjörður, Reykjavíkurvegi': 'or_006',
    'Skógarhlíð': 'or_007',
    'Suðurströnd': 'or_008',
    'Austurströnd': 'or_008',
    'Egilsstaðir, Fagradalsbraut': 'or_009',
    'Egilsstöðum, Fagrad.': 'or_009',
    'Fagradalsbraut, Egilsstaðir': 'or_009',
    'Fagradalsbraut Egilsstaðir': 'or_009',
    'Eskifjörður': 'or_010',
    'Eskifirði': 'or_010',
    'Fáskrúðsfjörður': 'or_011',
    'Fáskrúðsfirði': 'or_011',
    'Hallormsstaður': 'or_012',
    'Hallormsstað': 'or_012',
    'Neskaupstaður': 'or_013',
    'Neskaupstað': 'or_013',
    'Reyðarfjörður': 'or_014',
    'Reyðarfirði': 'or_014',
    'Seyðisfjörður': 'or_015',
    'Seyðisfirði': 'or_015',
    'Skjöldólfsstaðir': 'or_016',
    'Skjöldólfsstöðum': 'or_016',
    'Skjöldólfsstaður': 'or_016',
    'Árskógssandur': 'or_017',
    'Árskógssandi': 'or_017',
    'Furuvellir': 'or_018',
    'Furuvellir, Akureyri': 'or_018',
    'Furuvellir Akureyri': 'or_018',
    'Furuvöllum': 'or_018',
    'Húsavík': 'or_019',
    'Hvammstangi': 'or_020',
    'Hvammstanga': 'or_020',
    'Mýrarvegur': 'or_021',
    'Mýrarvegi': 'or_021',
    'Mýrarvegur, Akureyri': 'or_021',
    'Mýrarvegur Akureyri': 'or_021',
    'Mývatn': 'or_022',
    'Mývatni': 'or_022',
    'Sauðárkrókur': 'or_023',
    'Sauðárkrók': 'or_023',
    'Bíldudalur': 'or_024',
    'Bíldudal': 'or_024',
    'Bolungarvík': 'or_025',
    'Ísafjörður': 'or_026',
    'Ísafirði': 'or_026',
    'Súðavík': 'or_027',
    'Akranesi Skagabraut': 'or_028',
    'Skagabraut, Akranes': 'or_028',
    'Skagabraut Akranes': 'or_028',
    'Borgarnes': 'or_029',
    'Borgarnesi': 'or_029',
    'Grundarfjörður': 'or_030',
    'Grundarfirði': 'or_030',
    'Hreðavatnsskáli': 'or_031',
    'Hreðavatnsskála': 'or_031',
    'Húsafell': 'or_032',
    'Húsafelli': 'or_032',
    'Ólafsvík': 'or_033',
    'Stykkishólmur': 'or_034',
    'Stykkishólmi': 'or_034',
    'Grindavík': 'or_035',
    'Keflavíkurflugvöllur': 'or_036',
    'Leifsstöð': 'or_036',
    'FLE': 'or_036',
    'Reykjanesbær': 'or_037',
    'Fitjar': 'or_037',
    'Fitjum': 'or_037',
    'Njarðvík': 'or_037',
    'Sandgerði': 'or_038',
    'Freysnes': 'or_039',
    'Freysnesi': 'or_039',
    'Hvolsvöllur': 'or_040',
    'Hvolsvelli': 'or_040',
    'Selfoss': 'or_041',
    'Stokkseyri': 'or_042',
    'Úthlíð': 'or_043',
    'Vestmannaeyjar': 'or_044',
    'Vestmannaeyjum': 'or_044',
    'Vík í Mýrdal': 'or_045',
    'Þorlákshöfn': 'or_046',
    'Birkimelur': 'or_047',
    'Birkimel': 'or_047',
    'Bústaðavegur': 'or_048',
    'Kleppsvegur': 'or_049',
    'Kleppsvegi': 'or_049',
    'Smárinn': 'or_050',
    'Hagasmári': 'or_050',
    'Hagasmára': 'or_050',
    'Suðurfell': 'or_051',
    'Vesturlandsvegur': 'or_052',
    'Vesturlandsvegi': 'or_052',
    'Hörgárbraut': 'or_053',
    'Hörgárbraut, Akureyri': 'or_053',
    'Hörgárbraut Akureyri': 'or_053',
    'Hveragerði, Austurmörk': 'or_054',
    'Hveragerði Austurmörk': 'or_054',
    'Austurmörk, Hveragerði': 'or_054',
    'Austurmörk Hveragerði': 'or_054',
    'Garðabær': 'or_055',
    'Garðabæ': 'or_055',
    'Miklabraut v. Kringluna': 'or_056',
    'Miklabraut við Kringlu': 'or_056',
    'Miklubraut suður': 'or_056',
    'Eiðistorg': 'or_057',
    'Eiðistorgi': 'or_057',
    'Skemmuvegur': 'or_058',
    'Skemmuvegi': 'or_058',
    'Spöngin': 'or_059',
    'Spönginni': 'or_059',
    'Egilsstaðir, Miðvangi': 'or_060',
    'Egilsstöðum, Miðvangi': 'or_060',
    'Miðvangur, Egilsstaðir': 'or_060',
    'Miðvangur Egilsstaðir': 'or_060',
    'Akranesi Smiðjuvöllum': 'or_062',
    'Smiðjuvellir, Akranes': 'or_062',
    'Smiðjuvellir Akranes': 'or_062',
    'Hveragerði, Sunnumörk': 'or_063',
    'Hveragerði Sunnumörk': 'or_063',
    'Sunnumörk, Hveragerði': 'or_063',
    'Sunnumörk Hveragerði': 'or_063',
    'Hraunbær': 'or_064',
    'Hraunbæ': 'or_064',
    'Baulan': 'or_065',
    'Baula': 'or_065',
    'Baulu': 'or_065',
    'Fellsmúli': 'or_066',
    'Fellsmúla': 'or_066',
    'Salavegur': 'or_067',
    'Salavegi': 'or_067',
    'Vatnagarðar': 'or_068',
    'Vatnagörðum': 'or_068',
    'Stekkjabakki': 'or_069',
    'Stekkjarbakki': 'or_069',
    'Stekkjarbakka': 'or_069',
    'Hæðarsmári': 'or_070',
    'Hæðarsnári': 'or_070',
    'Hæðasmári': 'or_070',
    'Hæðarsmára': 'or_070',
    'Möðrudalur': 'or_071',
    'Möðrudal': 'or_071',
    'Hella': 'or_072',
    'Hellu': 'or_072',
    'Einhella': 'or_073',
    'Lambhagavegur': 'or_074',
}
ORKAN_DISCOUNTLESS_STATIONS = [
    'or_000', 'or_006', 'or_007', 'or_021', 'or_029', 'or_041', 'or_048', 'or_049', 'or_051',
    'or_053', 'or_067', 'or_073'
]
# Orkan has a default 10 ISK discount with Orkan keychain
# See: https://www.orkan.is/afslaettir/
ORKAN_MINIMUM_DISCOUNT = 12.0

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
# https://www.atlantsolia.is/daelulykill/afslattur-og-allskonar/
ATLANTSOLIA_MINIMUM_DISCOUNT = 11.0

# N1 offers discount of minimum 10 ISK and 2 N1 points per liter according to the following page:
# https://www.n1.is/n1-kortid/
# -----------------------------------------------------------------------------------------------
# Discounts vary between individual customers based on various connections, info on minimum
# discount was unfortunately not stated on the N1 website but was received/confirmed via email
# communication.
# -----------------------------------------------------------------------------------------------
N1_MINIMUM_DISCOUNT = 10.0
N1_LOCATION_RELATION = {
    'Ártúnshöfði': 'n1_000',
    'Bíldshöfði': 'n1_001',
    'Gagnvegur': 'n1_002',
    'Háholt': 'n1_003',
    'Bjarkarholt': 'n1_003',
    'Borgartún': 'n1_004',
    'Fossvogur': 'n1_005',
    'Stórihjalli': 'n1_006',
    'Verslun Stórihjalli': 'n1_006',
    'Lækjargata': 'n1_007',
    'Hringbraut': 'n1_008',
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
    'Verslun Ólafsvík': 'n1_075',
    'Flókalundur': 'n1_076',
    'Ægisíða': 'n1_077',
    'Knútstöð Keflavíkurflugvelli': 'n1_078',
    'Vallarheiði': 'n1_078',
    'Norðlingaholt': 'n1_079',
    'Víðihlíð': 'n1_080',
    'Lindir': 'n1_081',
    'Skógarlind': 'n1_081',
    'Norðurhella': 'n1_082',
    'Skútuvogi': 'n1_084',
    'Skútuvogur': 'n1_084',
    'Flugvellir': 'n1_085',
    'Fiskislóð': 'n1_086',
}
N1_DISCOUNTLESS_STATIONS = ['n1_011', 'n1_074', 'n1_081', 'n1_082', 'n1_079', 'n1_086']

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

BOT_UA = 'Mozilla/5.0 (compatible; Googlebot/2.1;+http://www.google.com/bot.html)'

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
    },
    {
        'timestamp_text': '2023-06-15T23:00',
        'commit_hash': 'b1b0a413303de2aef7bf37b711576a116a4b45bd',
        'note': 'N1 zero prices'
    },
    {
        'timestamp_text': '2023-06-16T04:15',
        'commit_hash': '0bebbe40af1d3515700064b962a1e3fc218094a7',
        'note': 'N1 zero prices'
    },
    {
        'timestamp_text': '2023-06-19T10:45',
        'commit_hash': 'fc44024f3191112961f30c39d9783865b553b0cb',
        'note': 'Orkan 10th low price (30.6 instead of 306)'
    },
    {
        'timestamp_text': '2023-07-07T18:00',
        'commit_hash': 'fbaca0f17e1b467fe0981f1a9d2d33eca0d40ef6',
        'note': 'N1 zero prices'
    }
]
