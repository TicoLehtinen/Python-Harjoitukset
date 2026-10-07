## Roskasankari THE kierrätyspeli

## Tico Lehtinen

## Peliprojektissa on tällä hetkellä intro.txt, ohjeet.txt, itse peli roskasankari.py ja readme.md tiedostot. tallennus.txt luodaan automaattisesti, kun pelaaja joko lopettaa pelin tai tallentaa pelin, joten sitä ei tarvitse olla valmiina erikseen.

## Tein Projekti 2 tehtävän valmiiksi ja lisäsin muutaman komennon peliin, jotka eivät kyllä vielä tee mitään varsinaiseti.

## Tein Projekti 3 tehtävän. Lisäsin funktiot ja korvasin while, if ja elif komennot siten, että ennen ne tulostivat vain tietyn tekstin komentoon liittyen, mutta nyt ne suorittavat funktion ja tulostavat tekstin, joka on jo lisättynä itse funktioon. Muokkasin myös "Päävalikkoa" vähän selkeämmäksi ja "hienommaksi".

## Tein Projekti 4 tehtävän, lisäsin luokat: pelaaja, huone ja esine ja annoi niille vaaditut ominaisuudet ja methodit / toiminnot.

## Tein Projekti 5 tehtävän, tein intro.txt ja ohjeet.txt tiedostot ja kirjoitin sinne intron pelille, sekä ohjetiedostoon pelinohjeet, mitä mikäkin komento tekee yms. Tein myös mahdollisuuden tallentaa pelin (joko tallenna tai lopeta kommennolla) ja se tiedosto luodaan vasta, kun käyttäjä/pelaaja antaa jomman kumman komennon. Peliä voi jatkaa, jos syöttää saman nimen, kuin mikä edellisellä kerralla oli käytössä peliä pelatessa. Tiedostoon tallennettaan vain yksi pelaaja, jos joku uusi hahmo tehdään ja sillä pelataan, sekä tallennettaan peli, niin edellinen peli ylikirjoitetaa.
---------------------------------------------------------------------------------------------------------------------------------

                                                                                                                               Roskasankari THE kierrätyspeli

                                                                                                                                 ## PELIN IDEA JA TARINA ##

                                                                                           Roskasankari kierrätyspeli, jossa pelaaja työskentelee kierrätyskeskuksessa ja lajittelee roskia oikeisiin roskiksiin. 
                                        Pelaaja on aloittanut työt Kierrätyskeskuksessa. Pomo odottaa ja vaatii, että roskat lajitellaan oikein. Lajittelupisteeseen tulee jatkuvasti uusia roskia, kuten muovipulloja, lasipurkkeja, tölkkejä ja banaaninkuoria. Pelaaja kerää roskat reppuunsa ja lajittelee ne oikeaan roskikseen.

                                                                     Oikea lajittelu antaa +10 pistettä ja virheellinen lajittelu vie 5 pistettä. Pelaajan työpaikka ja maine riippuvat siitä, miten hyvin hän lajittelee roskia työpäivänsä aikana.
                                                    
                                                                                                                                      ## TAVOITE ##

                                    Pelaajan tavoite on kerätä 100 pistettä lajittelemalla roskat oikein. Jos pisteet loppuvat eli pelaajalla on vain 0 pistettä, pelaaja menettää työpaikkansa ja peli päättyy pomon huutoihin. Peli voi päättyä myös ylennykseen, jos pelaaja tutustuu kierrätysoppaaseen ja osoittaa osaamisensa pomolle.

                                                                                                                                  ## MITEN PELI TOIMII ##

                                                                                       Pelaaja voi heti alussa mennä mihin tahansa huoneeseen, mutta roskia voi kerätä ja lajitella vain lajittelupisteellä.
      Pelaaja komentojen avulla pelaa peliä, jos pelaaja menee lajittelupisteeseen ja käyttää komentoa "kerää", hän kerää jonkin arvotun esineen ja esineitä voi kerätä korkeintaan 1 kilon verran, sillä jokaisella esineellä on oma painonsa ja pelaajan inventaarioon/reppuun mahtuu vain kilon verran esineitä. Jos pelaaja yrittää
                                                                                    kerätä enemmän kuin kilon, peli ilmoittaa, että ennen uusien roskien keräilyä, täytyy pelaajan ensin lajitella nykyiset roskat/tavarat.
   Pelaaja lajittelee roskia niin kauan, kunnes hän saavuttaa joko täydet 100 pistettä, jolloin hän voittaa pelin tai lajittelee esineitä niin kauan väärin, kunnes hänellä on 0 pistettä jäljellä ja hän häviää pelin. Pelissä on myös kolmas mahdollisuus pelata peli läpi, joka vaatii pelaajalta vähän pelin ja huoneiden tutkimista.
Pelaaja voi käyttää "tutki" komentoa pomon huoneessa, sekä taukohuoneessa. Jos pelaaja käyttää "tutki" komentoa pomon huoneessa ennen taukohuonetta, pomo kehottaa pelaajaa käymään ensin taukohuoneessa. Taukohuoneessa "tutki" komentoa käyttämällä pelaaja lukee pöydällä olevan kierrätysoppaan. Jos pelaaja menee sen jälkeen pomon huoneeseen, kehuu pomo pelaajaa oppaan lukemisesta ja kertoo kuinka monta esinettä (5 alussa) pelaajan täytyy vielä lajitella oikein, jotta pelaaja voi saada ylennyksen (ja voittaa pelin sillä tavalla)

                                                                                                               ## MITEN KESTÄVÄN KEHITYKSEN NÄKÖKULMA ON OTETTU PELISSÄ HUOMIOON? ##
                                       Koko pelin pääteemana on kestävä kehitys roskien oikeaoppisen lajittelun avulla. Kun lajittelet jätteet / roskat niihin kuuluviin astioihin / roskiksiin, voidaan ne kierrättää oikeaoppisesti ja käyttää uudelleen materiaalina.