
# Gasvaktin

![Gasvaktin](https://gasvaktin.is/images/gasvaktin.png)

Gasvaktin aims to be an open and automated price lookup project for petrol stations in Iceland (95 octan bensin and diesel).

Check out [gasvaktin.is](https://gasvaktin.is/) if you're travelling Iceland and want to find your preferred petrol station in your near vicinity.

If you're interested in working with the current petrol price data and/or historic data feel free to do so, the data is available within this repository, and the historic data is accessible via the git history, just fork and clone it to your local machine and use tools of your own choosing to read the data from the git history. If you're doing data analysis for some audience, public or private, be a good sport and mention origin of data, your audience will appreciate it and think higher of you for providing it.

If you notice any issues or errors please contact maintainer, or submit a PR to fix the issue.

Gasvaktin watches the following Icelandic oil companies:

* [Atlantsolía](http://atlantsolia.is/)
* [Costco Iceland](http://costco.is/)
* [N1](https://www.n1.is/)
* [Olís](http://www.olis.is/)
  - [ÓB](http://www.ob.is/) (low-cost company owned by Olís)
* [Skeljungur](http://www.skeljungur.is/)
  - [Orkan](http://www.orkan.is/) (low-cost company owned by Skeljungur)

## Setup and usage

You need to install [Python (3.6.8 or newer) and pip](https://docs.python-guide.org/starting/install3/win/) and install the following python modules:

	pip install -r pip_requirements.txt

You also need Firefox (version 78 or newer) and geckodriver installed for Selenium which is currently used to fetch prices for Orkan.

Open a terminal in this repository and

	python gasvaktin.py --collect-and-write-data

This updates the pretty `vaktin/gas.json` and the minified `vaktin/gas.min.json` with newest price data from the oil companies webpages. This is run every 15 minutes and in case of price changes they are automatically commited to the repository.

Run `python gasvaktin.py --help` to see available input arguments.

## Origination of data

Data over petrol stations and locations is currently just static. Price data from the oil companies is fetched regularly.

If you're interested in price trends over time, it can be extracted from git history via the following:

	cd scripts
	python trends.py

Run `python trends.py --help` to see available input arguments.

### Atlantsolía

#### Stations

Atlantsolía has a list of its stations [here](https://www.atlantsolia.is/stodvar/).

#### Prices

Gas price for each station can be found [here](https://www.atlantsolia.is/stodvaverd/), also showing discount prices available if you have Atlantsolía fuel key ring.

### Costco Iceland

#### Stations

Costco Iceland has a single petrol station in Iceland, in Kauptún next to IKEA. Note that you can't buy petrol at this station unless you're a Costco member, Costco membership card in Iceland costs ~5.000 ISK (~49 USD) annually.

#### Prices

Costco Iceland doesn't plan on showing their petrol prices on their web, at least not in the near future, so we currently have no way of tracking their prices except reading it straight off their pumps in Kauptún. We check and update their prices from time to time in [this Google Docs Spreadsheet](https://docs.google.com/spreadsheets/d/18xuZbhfInW_6Loua3_4LE7KxbGPsh-_3IFfLpf3uwYE/) but due to this procedure not being automatic, prices may not be correct from time to time.

### N1

#### Stations

N1 station locations can be viewed [here](https://www.n1.is/stodvar/).

#### Prices

Prices for N1 can be found [here](https://www.n1.is/thjonusta/eldsneyti/daeluverd/), you can find information on special fuel card discount [here](https://www.n1.is/n1-kortid/saekja-um-kortid/).

### Olís (and ÓB)

#### Stations

List of stations can be seen [here](http://www.olis.is/solustadir/thjonustustodvar) but unfortunately no geo coordinates seem to be exposed. We might be able to do automatic lookup on for example google maps and use that but manual review would probably always be needed. This is one of the reasons stations data is static.

#### Prices

Prices for Olís can be seen [here](http://www.olis.is/solustadir/thjonustustodvar/eldsneytisverd/) and prices for ÓB can be seen [here](http://www.ob.is/eldsneytisverd/), you can find information on special fuel key ring discount [here](https://www.olis.is/vidskiptakort/olis-lykill).

### Skeljungur (Orkan)

#### Stations

In the beginning of 2018 Skeljungur rebranded its remaining stations to Orkan, there are no fuel stations operating under the Skeljungur brand anymore. Also, it seems the Orkan X brand is no more too, with the last Orkan X station being rebranded to Orkan in either late 2019 or beginning of 2020. Skeljungur bought Dælan in 2020-11 ([previously owned by N1](https://twitter.com/gasvaktin/status/1082985305278464000)) and started rebranding the stations to Orkan stations in 2021-09 and finished rebranding the last station in 2021-11.

List of stations for Orkan can be seen [here](https://www.orkan.is/orkan/orkustodvar/).

#### Prices

Prices for Orkan individual stations can be seen [here](https://www.orkan.is/orkustodvar/). Information on special fuel key ring discount is shown [here](https://www.orkan.is/afslattur/).

## Maintainer

[@Loknar](https://github.com/Loknar/)

## Licence

MIT Licence
