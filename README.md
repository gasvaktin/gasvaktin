
# Gasvaktin

Gasvaktin aims to be an open and automated price lookup project for petrol stations in Iceland (95 octan bensin and diesel).

Gasvaktin watches the following Icelandic oil companies:

* [Atlantsolía](http://atlantsolia.is/)
* [N1](https://www.n1.is/)
* [Olís](http://www.olis.is/)
  - [ÓB](http://www.ob.is/) (low-cost company owned by Olís)
* [Skeljungur](http://www.skeljungur.is/)
  - [Orkan](http://www.orkan.is/) (low-cost company owned by Skeljungur)

## Setup and usage

You need to have [python 2.7 and pip](http://docs.python-guide.org/en/latest/starting/install/win/) and install the following python modules:

	pip install -r pip_requirements.txt

Open a terminal in this repository and

	cd scripts
	python pricer.py

This updates the pretty `vaktin/gas.json` and the minified `vaktin/gas.min.json` with newest price data from the oil companies webpages. The script `pricer.py` is run daily and price changes if any are automatically commited to the repository.

## Origination of data

Data over petrol stations and locations is currently just static. Price data from the oil companies is fetched on a daily basis.

### Atlantsolía

#### Stations

Atlantsolía has a list of its stations [here](http://atlantsolia.is/nav/StodvarStadsetningar.aspx). Looking at the source stations data is available in the following format:

	var LocationsMarker = [['Akureyri+Baldursnes', 65.6991300000000, -18.135231, 0,'<div ></div>','/images/stadsetningar_netid.gif'],['Akureyri+Gler%c3%a1rtorg', 65.6878070000000, -18.100104, 1,'<div ></div>','/images/stadsetningar_netid.gif'],['B%c3%adldsh%c3%b6f%c3%b0i', 64.1253970000000, -21.813054, 2,'<div ></div>','/images/stadsetningar_netid.gif'],['Borgarnes', 64.5675445000000, -21.8934511, 3,'<div ></div>','/images/stadsetningar_netid.gif'], ...

#### Prices

Gas price for each station can be found [here](http://atlantsolia.is/stodvarverd.aspx), also showing discount prices available if you have Atlantsolía gas key ring.

### N1

#### Stations

List of stations can be found [here](https://www.n1.is/stodvar/). With a bit of examination we can see a JSON endpoint which exposes stations list and location info. Example:
	
	POST https://www.n1.is/umbraco/api/stations/get
	Headers = {
		Cookie: _ga=GA1.2.789097346.1420231531; StoreInfo=StoreAlias=IS
		User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36
	}

#### Prices

List price (price without any discount) can be seen [here](https://www.n1.is/listaverd/), discount price given if you have an N1 business card can be seen [here](https://www.n1.is/eldsneyti). We assume these prices to be global for all N1 stations as we can't find station individual prices anywhere.

### Olís (and ÓB)

#### Stations

List of stations can be seen [here](http://www.olis.is/solustadir/thjonustustodvar) but unfortunately no geo coordinates seem to be exposed. We might be able to do automatic lookup on for example google maps and use that but manual review would probably always be needed. This is one of the reasons stations data is static.

#### Prices

Prices for Olís can be seen [here](http://www.olis.is/solustadir/thjonustustodvar/eldsneytisverd/) and prices for ÓB can be seen [here](http://www.ob.is/eldsneytisverd/), both with and without special gas key ring discount.

### Skeljungur (and Orkan (and Orkan X))

#### Stations

List of stations for Skeljungur, Orkan and Orkan X can be seen [here](http://www.skeljungur.is/einstaklingar/stadsetning-stodva/). With a bit of examination like with N1 we can see a JSON endpoint/file which exposes stations list and location info. Example:

	GET http://www.skeljungur.is/LisaLib/GetSupportFile.aspx?id=d070afa9-d1ff-11e4-80e4-005056a6135c

#### Prices

Prices without discount for Skeljungur and Orkan can be seen [here](http://www.skeljungur.is/einstaklingar/eldsneytisverd/), and station individual prices for Orkan X can be found [here](http://www.orkan.is/Orkan-X/Stodvar). Info on discount for Orkan can be seen [here](https://www.orkan.is/Afslattarthrep), but it's threefold when this is written (5/7/10 ISK discount) and is controlled by how much gas you bought from Orkan the month before. To make things easier we only provide discount price for the starter discount. Neither Skeljungur nor Orkan X maintain a discount program.

## Maintainer

[@Loknar](https://github.com/Loknar/)

## Licence

MIT Licence
