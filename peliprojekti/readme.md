## Roskasankari THE kierrätyspeli

## Tico Lehtinen

## Peliprojektissa on tällä hetkellä intro.txt, ohjeet.txt, itse peli roskasankari.py ja readme.md tiedostot. tallennus.txt luodaan automaattisesti, kun pelaaja joko lopettaa pelin tai tallentaa pelin, joten sitä ei tarvitse olla valmiina erikseen.

## Tein Projekti 2 tehtävän valmiiksi ja lisäsin muutaman komennon peliin, jotka eivät kyllä vielä tee mitään varsinaiseti.

## Tein Projekti 3 tehtävän. Lisäsin funktiot ja korvasin while, if ja elif komennot siten, että ennen ne tulostivat vain tietyn tekstin komentoon liittyen, mutta nyt ne suorittavat funktion ja tulostavat tekstin, joka on jo lisättynä itse funktioon. Muokkasin myös "Päävalikkoa" vähän selkeämmäksi ja "hienommaksi".

## Tein Projekti 4 tehtävän, lisäsin luokat: pelaaja, huone ja esine ja annoi niille vaaditut ominaisuudet ja methodit / toiminnot.

## Tein Projekti 5 tehtävän, tein intro.txt ja ohjeet.txt tiedostot ja kirjoitin sinne intron pelille, sekä ohjetiedostoon pelinohjeet, mitä mikäkin komento tekee yms. Tein myös mahdollisuuden tallentaa pelin (joko tallenna tai lopeta kommennolla) ja se tiedosto luodaan vasta, kun käyttäjä/pelaaja antaa jomman kumman komennon. Peliä voi jatkaa, jos syöttää saman nimen, kuin mikä edellisellä kerralla oli käytössä peliä pelatessa. Tiedostoon tallennettaan vain yksi pelaaja, jos joku uusi hahmo tehdään ja sillä pelataan, sekä tallennettaan peli, niin edellinen peli ylikirjoitetaa.
---------------------------------------------------------------------------------------------------------------------------------
# Roskasankari THE KIERRÄTYSPELI

Tekstipohjainen kierrätyspeli, jossa pelaaja työskentelee kierrätyskeskuksessa ja lajittelee roskia oikeisiin roskiksiin.

## Pelin idea ja tarina

Pelaaja on aloittanut työt kierrätyskeskuksessa. Pomo odottaa ja vaatii, että roskat lajitellaan oikein. Lajittelupisteeseen tulee jatkuvasti uusia roskia, kuten muovipulloja, lasipurkkeja, tölkkejä ja banaaninkuoria. Pelaaja kerää roskat reppuunsa ja lajittelee ne oikeaan roskikseen.

Oikea lajittelu antaa +10 pistettä ja virheellinen lajittelu vie -5 pistettä. Pelaajan työpaikka ja maine riippuvat siitä, kuinka hyvin hän lajittelee roskia työpäivänsä aikana.

## Tavoite

Tavoitteena on kerätä 100 pistettä lajittelemalla roskat oikein. Jos pisteet loppuvat eli pelaajalla on vain 0 pistettä, hän menettää työpaikkansa ja peli päättyy pomon huutoihin. Peli voi päättyä myös ylennykseen, jos pelaaja tutustuu kierrätysoppaaseen ja osoittaa osaamisensa pomolle.

## Pelin loput

| Loppu | Miten saavutetaan |
|---|---|
| Voitto | Kerää 100 pistettä |
| Ylennys | Lue opas taukohuoneessa, lajittele 5 roskaa oikein ja käy pomon luona |
| Häviö | Pisteet putoavat nollaan |

## Miten peli toimii

- Pelaaja voi liikkua huoneiden välillä vapaasti, mutta roskia voi kerätä ja lajitella vain Lajittelupisteessä.
- Komennolla "kerää" pelaaja saa arvotun esineen. Reppuun mahtuu enintään 1 kg roskia, ja jokaisella esineellä on oma painonsa. Jos reppu on täynnä, pelaajan täytyy lajitella ensin nykyiset roskat.
- Pelaaja lajittelee roskia, kunnes hän voittaa tai pisteet loppuvat.
- Pomon huoneessa ja taukohuoneessa voi käyttää komentoa "tutki":
  - Taukohuoneessa pelaaja lukee kierrätysoppaan, joka antaa vinkkejä lajitteluun.
  - Jos pelaaja menee pomon huoneeseen ennen taukohuonetta, pomo käskee käymään ensin taukohuoneessa.
  - Oppaan luettuaan pomo kertoo, montako esinettä (5 alussa) pelaajan täytyy vielä lajitella oikein ylennystä varten.

## Komennot

| Komento | Mitä tekee? |
|---|---|
| "aloita" | Aloittaa pelin (alkuvalikossa) |
| "liiku" | Siirtyy toiseen huoneeseen |
| "kerää" | Kerää roskan reppuun |
| "lajittele" | Lajittelee repun esineen roskikseen |
| "tutki" | Tutkii huoneen (opas / pomo) |
| "esineet" | Näyttää repun sisällön |
| "pisteet" | Näyttää pisteet |
| "tallenna" | Tallentaa pelin |
| "ohje" | Näyttää ohjeet |
| "lopeta" | Tallentaa ja lopettaa |

## Miten kestävän kehityksen näkökulma on otettu pelissä huomioon?

Koko pelin pääteemana on kestävä kehitys roskien oikeaoppisen lajittelun avulla. Kun lajittelet jätteet oikeisiin roskiksiin, voidaan ne kierrättää oikeaoppisesti ja käyttää uudelleen materiaalina. Oikein lajitellessa pelaaja saa myös tietoa kierrätyksen hyödyistä.