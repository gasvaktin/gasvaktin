
# GasVaktin

GasVaktin er sjálfvirk verðvakt sem fylgist með verði á eldsneyti (95 octan bensín og díesel) hjá olíufélögum á Íslandi.

GasVaktin athugar verðupplýsingar hjá eftirfarandi olíufélögum:

* [Atlantsolía](http://atlantsolia.is/)
* [N1](https://www.n1.is/)
* [Olís](http://www.olis.is/)
  - [ÓB](http://www.ob.is/) (lággjaldafélag í eigu Olís)
* [Skeljungur](http://www.skeljungur.is/)
  - [Orkan](http://www.orkan.is/) (lággjaldafélag í eigu Skeljungs)

## Upplýsingar um uppruna gagna

Gögn yfir stöðvar olíufélaganna eru eins og er harðkóðuð. Verðgögn eru sótt af vefsíðum olíufélaganna daglega.

### Atlantsolía

#### Stöðvar

Atlantsolía er með einfaldan og góðan lista yfir stöðvarnar sínar á einföldu google maps korti sem sýnt er [á vef þeirra](http://atlantsolia.is/nav/StodvarStadsetningar.aspx). Þegar source er skoðað má sjá geo staðsetningar fyrir stöðvar Atlantsolíu svona útlítandi:

	var LocationsMarker = [['Akureyri+Baldursnes', 65.6991300000000, -18.135231, 0,'<div ></div>','/images/stadsetningar_netid.gif'],['Akureyri+Gler%c3%a1rtorg', 65.6878070000000, -18.100104, 1,'<div ></div>','/images/stadsetningar_netid.gif'],['B%c3%adldsh%c3%b6f%c3%b0i', 64.1253970000000, -21.813054, 2,'<div ></div>','/images/stadsetningar_netid.gif'],['Borgarnes', 64.5675445000000, -21.8934511, 3,'<div ></div>','/images/stadsetningar_netid.gif'], ...

#### Eldsneytisverð

Verð á eldsneyti fyrir allar stöðvar Atlantsolíu má finna á [þessari síðu](http://atlantsolia.is/stodvarverd.aspx) á vef Atlantsolíu, einnig má sjá þar afsláttarverð sem fæst með notkun dælulyklils Atlantsolíu. Að vísu virðist verðið ávallt vera það sama á öllum stöðvum nema einni sem virðist þá ávallt vera ódýrari, daginn sem þetta er skrifað til dæmis (2016-04-10) er Atlantsolía Kópavogi Skemmuvegi 4 ISK ódýrari en aðrar stöðvar Atlantsolíu.

### N1

#### Stöðvar

Hægt er að nálgast lista yfir bensínstöðvar N1 á síðu þeirra á svotilgerðu [gagnvirku stöðva-korti](https://www.n1.is/stodvar/). Með örlítilli eftirgrennslan er hægt að finna einfaldan JSON endapunkt sem gefur ítarlegar upplýsingar um N1 stöðvar um allt landið, auk staðsetningarhnita.
	
	POST https://www.n1.is/umbraco/api/stations/get
	Headers = {
		Cookie: _ga=GA1.2.789097346.1420231531; StoreInfo=StoreAlias=IS
		User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36
	}

Þetta gefur JSON lista yfir stöðvar, verslanir og verkstæði N1. Auðvelt er að veiða stöðvar sem selja í það minnsta 95 octan bensín, diesel olíu, og eru ekki Bátadælur.

#### Eldsneytisverð

Á [N1 Listaverð](https://www.n1.is/listaverd/) má sjá listaverð N1 á bensíni og dísel en verð með afslætti N1 Kortsins er hægt að sjá á [N1 Eldsneyti](https://www.n1.is/eldsneyti). Þetta eru einu verðupplýsingar sem við höfum aðgang að hjá N1 og þurfum við því (ranglega eða réttilega) að gera ráð fyrir að þetta verð gildi fyrir allar N1 stöðvar.

### Olís (og ÓB)

#### Stöðvar

Á vef Olís má skoða [einfalt íslandskort](http://www.olis.is/solustadir/thjonustustodvar) sem sýnir þjónustustöðvar fyrir bæði Olís og ÓB. Ef rýnt er í html síðunnar má sjá `<div id="stodvakort">` sem inniheldur alla punktana á kortinu, en því miður koma staðsetningar einungis fram á svona formi `top: 197px;left: 86px;`, engin hnit exposuð. Mögulega er hægt að reikna grófa staðsetningu út frá þessum punktum eða fletta einhvernveginn sjálfvirkt upp stöðvunum til dæmis Google Maps fyrir nákvæmari hnit hverrar stöðvar.

#### Eldsneytisverð

Hægt er að nálgast á bæði [vef Olís](http://www.olis.is/solustadir/thjonustustodvar/eldsneytisverd/) og [vef ÓB](http://www.ob.is/eldsneytisverd/) eldsneytisverð með og án sérstaks korta- eða dælulykilsafsláttar.

### Skeljungur (og Orkan (og Orkan X))

#### Stöðvar

Lista yfir stöðvar Skeljungs og undirfélaganna Orkan og Orkan X má sjá [hér á vef Skeljungs](http://www.skeljungur.is/einstaklingar/stadsetning-stodva/). Líkt og með N1 er enfaldur JSON 'endapunktur' sem gefur lista stöðva um allt land sem og staðsetningarhnit.

	GET http://www.skeljungur.is/LisaLib/GetSupportFile.aspx?id=d070afa9-d1ff-11e4-80e4-005056a6135c

#### Eldsneytisverð

Verð fyrir Skeljung/Orkuna/Orkuna X má finna [hér á vef Skeljungs](http://www.skeljungur.is/einstaklingar/eldsneytisverd/). Upplýsingar um afslátt hjá Orkunni er síðan hægt að skoða [hér  á vef Orkunnar](https://www.orkan.is/Afslattarthrep), en hann er þrískiptur þegar þetta er skrifað (5/7/10 kr afsláttur) og stýrist af viðskiptum einstaklings mánuðinn á undan. Til hægðarauka reiknum við einfaldlega með minnsta afslættinum þar sem hann er aðgengilegur öllum með Orku-lykil. Stöðvar Skeljungs og Orkunnar X bjóða engan sérstakan afslátt, Skeljungur leggur í staðinn áherslu á góða þjónustu, en Orkan X hefur það að auðkenni að hafa gott lágt verð fyrir alla í stað þess að leika afsláttaleikinn svokallaða. Eitt merkilegt þó við Orku X stöðvarnar er að ein þeirra, Orkan X Skemmuvegi, er 5 krónum ódýrari en aðrar Orkan X stöðvar þegar þetta er skrifað.

## Maintainers

[@Loknar](https://github.com/Loknar/)

Hafi einhver áhuga á að gerast maintainer hafið þá samband við [@Loknar](https://github.com/Loknar/).

## Skilmálar

MIT Licence
