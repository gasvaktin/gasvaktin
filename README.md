
# Gasvaktin

Gasvaktin aims to be an open and automated price lookup project for petrol stations in Iceland (95 octan bensin and diesel).

Check out [gasvaktin.is](https://gasvaktin.is/) if you're travelling Iceland and want to find your preferred petrol station in your near vicinity.

Follow [Gasvaktin on Twitter](https://twitter.com/gasvaktin/status/861277070621638656) if you'd like to be notified on price changes, they're automatically tweeted by [@gasvaktin](https://twitter.com/gasvaktin) when detected.

If you're interested in working with the current petrol price data provided there is a publicly available API endpoint which exposes current price data, the API is hosted by the awesome icelandic [apis.is](http://docs.apis.is/#endpoint-petrol) project, check it out.

If you notice any issues or errors please contact maintainer, or submit a PR to fix the issue.

Gasvaktin watches the following Icelandic oil companies:

* [Atlantsolía](http://atlantsolia.is/)
* [Costco Iceland](http://costco.is/)
* [N1](https://www.n1.is/)
* [Dælan](http://daelan.is/) (low-cost company [previously owned by N1](https://twitter.com/gasvaktin/status/1082985305278464000))
* [Olís](http://www.olis.is/)
  - [ÓB](http://www.ob.is/) (low-cost company owned by Olís)
* [Skeljungur](http://www.skeljungur.is/)
  - [Orkan](http://www.orkan.is/) (low-cost company owned by Skeljungur)

## Setup and usage

You need to install [Python3 (3.6.8 or newer) and pip](https://docs.python-guide.org/starting/install3/win/) and install the following python modules:

	pip install -r pip_requirements.txt

Note: Either make sure Python3 is set to default over Python2, or use `python3` and `pip3` instead of `python` and `pip`. Python2 lifecycle ends in 2019, so hopefully we can stop worrying about default Python in 2020.

Open a terminal in this repository and

	python3 gasvaktin.py --collect-and-write-data

This updates the pretty `vaktin/gas.json` and the minified `vaktin/gas.min.json` with newest price data from the oil companies webpages. This is run every 15 minutes and in case of price changes they are automatically commited to the repository.

Run `python gasvaktin.py --help` to see available input arguments.

## Origination of data

Data over petrol stations and locations is currently just static. Price data from the oil companies is fetched regularly. See [here](https://gist.github.com/gasvaktin) for more details on when prices were last checked.

If you're interested in price trends over time, it can be extracted from git history via the following:

	cd scripts
	python trends.py

Run `python trends.py --help` to see available input arguments.

### Atlantsolía

#### Stations

Atlantsolía has a list of its stations [here](https://www.atlantsolia.is/stodvar/).

#### Prices

Gas price for each station can be found [here](http://atlantsolia.is/stodvarverd.aspx), also showing discount prices available if you have Atlantsolía fuel key ring.

### Costco Iceland

#### Stations

Costco Iceland has a single petrol station in Iceland, in Kauptún next to IKEA. Note that you can't buy petrol at this station unless you're a Costco member, Costco membership card in Iceland costs ~5.000 ISK (~49 USD) annually.

#### Prices

Costco Iceland doesn't plan on showing their petrol prices on their web, at least not in the near future, so we currently have no way of tracking their prices except reading it straight off their pumps in Kauptún. We check and update their prices from time to time in [this Google Docs Spreadsheet](https://docs.google.com/spreadsheets/d/18xuZbhfInW_6Loua3_4LE7KxbGPsh-_3IFfLpf3uwYE/) but due to this procedure not being automatic, prices may not be correct from time to time.

### N1

#### Stations

List of stations can be found [here](https://www.n1.is/stodvar/). With a bit of examination we can see a JSON endpoint which exposes stations list and location info. Example:
	
	POST https://www.n1.is/umbraco/api/stations/get
	Headers = {
		Cookie: _ga=GA1.2.789097346.1420231531; StoreInfo=StoreAlias=IS
		User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36
	}

#### Prices

Once it was possible to view a single global price [here](https://www.n1.is/eldsneyti/), however around 2018-05 N1 added [a note basicly stating the provided price might not be entirely global](https://github.com/gasvaktin/gasvaktin/commit/c308d1a7b5e088ddf8ef99f3ca00aa29af39019e). As time passed more and more stations became price deviants, attempts have been made to add information on the deviants based on real life observations which are kept [here](https://github.com/gasvaktin/gasvaktin/blob/master/scripts/globs.py#L265-L302). At some point in time during the summer 2019 fuel prices stopped showing up on the N1 website, however the JSON endpoint we've been accessing hasn't been removed yet so we can still access the global prices they once displayed on their website. We assume these prices to be global for all N1 stations, however we know there are deviant stations and out there, and prices for deviants currently just have hardcoded shift values from the provided global prices. [ :heart: Hopefully N1 will simply add individual fuel price information for all stations to the website, so we can cease these deviant shenanigans. :heart: ]

Discount for N1 business card holders can be seen [here](https://www.n1.is/n1-kortid/saekja-um-kort/). At the time of this writing the discount amount is 5 ISK and 2 N1 points per liter, both for bensin and diesel.

### Dælan

#### Stations

Station locations for Dælan are shown on a picture of a map on [dælan.is](https://daelan.is/).

#### Prices

Dælan stations don't have any discount prices, prices are shown on [dælan.is](https://daelan.is/).

### Olís (and ÓB)

#### Stations

List of stations can be seen [here](http://www.olis.is/solustadir/thjonustustodvar) but unfortunately no geo coordinates seem to be exposed. We might be able to do automatic lookup on for example google maps and use that but manual review would probably always be needed. This is one of the reasons stations data is static.

#### Prices

Prices for Olís can be seen [here](http://www.olis.is/solustadir/thjonustustodvar/eldsneytisverd/) and prices for ÓB can be seen [here](http://www.ob.is/eldsneytisverd/), you can find information on special fuel key ring discount [here](https://www.olis.is/vidskiptakort/olis-lykill).

### Skeljungur (and Orkan (and Orkan X))

#### Stations

In the beginning of 2018 Skeljungur rebranded its remaining stations to Orkan, there are no fuel stations operating under the Skeljungur brand anymore.

List of stations for Orkan and Orkan X can be seen [here](https://www.orkan.is/orkan/orkustodvar/).

#### Prices

Prices for Orkan and Orkan X individual stations can be seen [here](https://www.orkan.is/orkan/orkustodvar/). Information on the [discount for Orkan (Afsláttarþrep)](https://www.orkan.is/orkan/serkjor/) is currently missing from the updated Orkan website, before the update there was information available that it's threefold (5/6/8 ISK discount) and is controlled by how much fuel you bought from Orkan the month before (extra +2 discount for user selected station). To simplify we only use the default minimum discount, currently 5 ISK. Orkan X does not maintain a discount program.

## Maintainer

[@Loknar](https://github.com/Loknar/)

## Licence

MIT Licence
