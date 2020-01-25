
# Gasvaktin

![Gasvaktin](https://gasvaktin.is/images/gasvaktin.png)

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

You need to install [Python (3.6.8 or newer) and pip](https://docs.python-guide.org/starting/install3/win/) and install the following python modules:

	pip install -r pip_requirements.txt

**Note:** Either make sure Python3 is set to default over Python2 in your environment, or use `python3` and `pip3` instead of `python` and `pip`. Python2 lifecycle ended in 2019, so hopefully we can stop worrying about default Python sometime in 2020.

Open a terminal in this repository and

	python gasvaktin.py --collect-and-write-data

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

N1 station locations can be viewed [here](https://www.n1.is/stodvar/).

#### Prices

Prices for N1 can be found [here](https://www.n1.is/thjonusta/eldsneyti/daeluverd/), you can find information on special fuel card discount [here](https://www.n1.is/n1-kortid/saekja-um-kortid/). At the time of this writing the minimum discount amount is 5 ISK and 2 N1 points per liter, both for bensin and diesel.

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

### Skeljungur (and Orkan)

#### Stations

In the beginning of 2018 Skeljungur rebranded its remaining stations to Orkan, there are no fuel stations operating under the Skeljungur brand anymore. Also, it seems the Orkan X brand is no more too, with the last Orkan X station being rebranded to Orkan in either late 2019 or beginning of 2020.

List of stations for Orkan can be seen [here](https://www.orkan.is/orkan/orkustodvar/).

#### Prices

Prices for Orkan and Orkan X individual stations can be seen [here](https://www.orkan.is/orkan/orkustodvar/). Information on the [discount for Orkan (Afsláttarþrep)](https://www.orkan.is/orkan/serkjor/) is currently missing from the updated Orkan website, before the update there was information available that it's threefold (5/6/8 ISK discount) and is controlled by how much fuel you bought from Orkan the month before (extra +2 discount for user selected station). To simplify we only use the default minimum discount, currently 5 ISK. Orkan X does not maintain a discount program.

## Maintainer

[@Loknar](https://github.com/Loknar/)

## Licence

MIT Licence
