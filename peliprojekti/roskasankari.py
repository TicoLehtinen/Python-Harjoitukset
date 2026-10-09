import json
import os
import random
import time
 
## Vakiot: pisteet, ikäraja ja repun painoraja
KANSIO = os.path.dirname(os.path.abspath(__file__))
TALLENNUSTIEDOSTO = os.path.join(KANSIO, "tallennus.json")
IKÄRAJA = 12
ALKUPISTEET = 20
VOITTOPISTEET = 100
OIKEA_PISTEET = 10
VIRHE_PISTEET = 5
REPUN_RAJA = 1.0
YLENNYS_OIKEIN = 5

## Lista lajiteltavien roskien "lajeista"
LAJIT = ["muovi", "lasi", "paperi", "metalli", "biojäte", "sekajäte"]
 
## Lista, jonka sisällä on monikko Roskat: nimi, paino ja oikea laji
ROSKAT = [
    ("Cokispullo", 0.1, "muovi"),
    ("Muovipussi", 0.05, "muovi"),
    ("Shampoopullo", 0.15, "muovi"),
    ("Lasipullo", 0.1, "lasi"),
    ("Lasiastia", 0.3, "lasi"),
    ("Sanomalehti", 0.3, "paperi"),
    ("Maitopurkki", 0.1, "paperi"),
    ("Säilyketölkki", 0.2, "metalli"),
    ("Juomatölkki", 0.05, "metalli"),
    ("Banaaninkuori", 0.1, "biojäte"),
    ("Puoliksi syöty omena", 0.1, "biojäte"),
    ("Rikkinäinen kahvikuppi", 0.25, "sekajäte"),
]
 
## Sanakirja Faktat, jotka näytetään, kun roska lajitellaan oikein
FAKTAT = {
    "muovi": "Kierrätetystä muovista voidaan tehdä uusia tuotteita, esim. polyester vaatteita.",
    "lasi": "Lasi voidaan kierrättää uudelleen ja uudelleen, ilman, että se heikkenee.",
    "paperi": "Kierrätyspaperi säästää luontoa ja energiaa.",
    "metalli": "Metallin kierrätys säästää paljon energiaa uuden valmistamiseen verrattuna.",
    "biojäte": "Biojätteestä voidaan tehdä biokaasua ja multaa.",
    "sekajäte": "Mitä paremmin lajittelet, sitä vähemmän jätettä päätyy poltettavaksi.",
}
 
 
## Esine-luokka
class Esine:
    def __init__(self, nimi, paino, laji):
        self.nimi = nimi
        self.paino = paino
        self.laji = laji
 
 
## Huone-luokka
class Huone:
    def __init__(self, nimi, kuvaus, toiminto=None):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.toiminto = toiminto
 
 
## Pelaaja-luokka
class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti
        self.esineet = []
        self.pisteet = ALKUPISTEET
        self.oikein = 0 
        self.opas_luettu = False
 
    ## Laskee repun painon yhteen.
    def repun_paino(self):
        yhteensä = 0
        for esine in self.esineet:
            yhteensä += esine.paino
        return round(yhteensä, 2)
 
    ## Arpoo roskan ja laittaa sen reppuun, jos se mahtuu. Toimii vain Lajittelupisteessä.
    def kerää_esine(self):
        if self.sijainti.nimi != "Lajittelupiste":
            print("Tässä huoneessa ei ole esineitä kerättäväksi.")
            return
        nimi, paino, laji = random.choice(ROSKAT)
        if self.repun_paino() + paino > REPUN_RAJA:
            print(f"Reppu on liian painava! Lajittele ensin (raja {REPUN_RAJA} kg).")
        else:
            self.esineet.append(Esine(nimi, paino, laji))
            print(f"Keräsit esineen: {nimi} (paino: {paino} kg)")
 
    ## Poistaa esineen repusta ja päivittää pisteet. Palauttaa True, jos laji oli oikea.
    def lajittele(self, esine, laji):
        self.esineet.remove(esine)
        if esine.laji == laji:
            self.pisteet += OIKEA_PISTEET
            self.oikein += 1
            return True
        self.pisteet = max(0, self.pisteet - VIRHE_PISTEET)
        return False
 
 
## Lukee tekstitiedoston (intro.txt tai ohjeet.txt) ja palauttaa sen tekstin
def lue_tiedosto(tiedostonimi):
    try:
        with open(os.path.join(KANSIO, tiedostonimi), "r", encoding="utf-8") as tiedosto:
            return tiedosto.read()
    except FileNotFoundError:
        return f"(Tiedostoa {tiedostonimi} ei löytynyt.)"
 
 
## Tallentaa pelin JSON-tiedostoon sanakirjana. Reppu tallennetaan esineiden nimillä.
def tallenna_peli(pelaaja):
    reppu = []
    for esine in pelaaja.esineet:
        reppu.append(esine.nimi)
 
    tiedot = {
        "nimi": pelaaja.nimi,
        "pisteet": pelaaja.pisteet,
        "oikein": pelaaja.oikein,
        "opas_luettu": pelaaja.opas_luettu,
        "sijainti": pelaaja.sijainti.nimi,
        "reppu": reppu,
    }
    with open(TALLENNUSTIEDOSTO, "w", encoding="utf-8") as tiedosto:
        json.dump(tiedot, tiedosto)
 
 
## Lukee tallennuksen. Jos tallennusta ei ole, ei palauta mitään. Except myös tarkistaa, että onko tallennus olemassa ja/tai onko se vioittunut, jotta ohjelma ei kaadu sen takia erroreihin.
def lue_tallennus():
    try:
        with open(TALLENNUSTIEDOSTO, "r", encoding="utf-8") as tiedosto:
            return json.load(tiedosto)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
 
 
## Tekee tallennuksen tiedoista takaisin Pelaaja-olion
def lataa_peli(tiedot, huoneet):
    sijainti = huoneet[0]
    for huone in huoneet:
        if huone.nimi == tiedot["sijainti"]:
            sijainti = huone
 
    pelaaja = Pelaaja(tiedot["nimi"], sijainti)
    pelaaja.pisteet = tiedot["pisteet"]
    pelaaja.oikein = tiedot["oikein"]
    pelaaja.opas_luettu = tiedot["opas_luettu"]
 
    for esineen_nimi in tiedot["reppu"]:
        for nimi, paino, laji in ROSKAT:
            if nimi == esineen_nimi:
                pelaaja.esineet.append(Esine(nimi, paino, laji))
    return pelaaja
 
 
## Poistaa tallennuksen, kun peli on päättynyt
def poista_tallennus(nimi):
    tiedot = lue_tallennus()
    if tiedot and tiedot["nimi"].lower() == nimi.lower():
        os.remove(TALLENNUSTIEDOSTO)
 
 
## Kysyy iän, kunnes pelaaja antaa numeron
def kysy_ikä():
    while True:
        print("Minkä ikäinen olet? ")
        vastaus = input()
        if vastaus.isdigit() and int(vastaus) > 0:
            return int(vastaus)
        print("Anna ikä numerona, esim. 12.")
 
 
## Luo huoneet ja palauttaa ne listana. Ensimmäinen huone on aloitushuone.
def luo_huoneet():
    lajittelupiste = Huone(
        "Lajittelupiste",
        "Täällä ovat roskikset ja roskia tulee niin paljon kuin jaksat niitä kantaa.",
    )
    pomon_huone = Huone(
        "Pomon huone",
        "Pomo katsoo sinua tiukasti silmiin. Ehkä hänellä on jotain asiaa sinulle... (tutki).",
        "pomo",
    )
    taukohuone = Huone(
        "Taukohuone",
        "Kahvinkeitin porisee kuumana. Pöydällä näyttäisi olevan jokin lappu (tutki).",
        "opas",
    )
    return [lajittelupiste, pomon_huone, taukohuone]
 
 
## Tulostaa vaihtoehdot numeroituna ja palauttaa valitun indeksin (None, jos valinta ei kelpaa)
def valitse_listasta(kysymys, vaihtoehdot):
    numero = 1
    for vaihtoehto in vaihtoehdot:
        print(f"  {numero}. {vaihtoehto}")
        numero += 1
    print(kysymys)
    vastaus = input().strip()
    if vastaus.isdigit() and 1 <= int(vastaus) <= len(vaihtoehdot):
        return int(vastaus) - 1
    return None
 
 
## Siirtää pelaajan valittuun huoneeseen
def liiku_huoneeseen(pelaaja, huoneet):
    nimet = []
    for huone in huoneet:
        nimet.append(huone.nimi)
 
    print("Huoneet, joihin voit siirtyä:")
    i = valitse_listasta("Minne haluat siirtyä? (numero) ", nimet)
    if i is None:
        print("Tuntematon huone.")
    else:
        pelaaja.sijainti = huoneet[i]
        print(f"Siirryit uuteen huoneeseen: {huoneet[i].nimi}")
        print(huoneet[i].kuvaus)
 
 
## Näyttää repun sisällön ja painon
def näytä_esineet(pelaaja):
    if len(pelaaja.esineet) == 0:
        print("Reppusi on tyhjä.")
    else:
        print("Repussasi on seuraavat esineet:")
        for esine in pelaaja.esineet:
            print("-", esine.nimi, f"({esine.paino} kg)")
        print(f"Yhteensä {pelaaja.repun_paino()} kg")
 
 
def näytä_pisteet(pelaaja):
    print(f"Pisteesi: {pelaaja.pisteet} / {VOITTOPISTEET}")
    print(f"Oikein lajiteltuja: {pelaaja.oikein}")
 
 
## Pelaaja valitsee esineen ja roskiksen. Pisteet päivittyvät.
def lajittele_roskat(pelaaja):
    if pelaaja.sijainti.nimi != "Lajittelupiste":
        print("Roskikset ovat Lajittelupisteessä. Mene sinne ensin.")
        return
    if len(pelaaja.esineet) == 0:
        print("Reppusi on tyhjä. Kerää ensin jotain lajiteltavaa.")
        return
 
    nimet = []
    for esine in pelaaja.esineet:
        nimet.append(esine.nimi)
 
    print("Mikä esine lajitellaan?")
    i = valitse_listasta("Valinta (numero): ", nimet)
    if i is None:
        print("Tuntematon valinta.")
        return
    esine = pelaaja.esineet[i]
 
    if pelaaja.opas_luettu:
        print(f"Oppaan vinkki: {esine.nimi} kuuluu kohtaan {esine.laji}.")
    print("Mihin roskikseen se menee?")
    j = valitse_listasta("Valinta (numero): ", LAJIT)
    if j is None:
        print("Tuntematon roskis.")
        return
 
    if pelaaja.lajittele(esine, LAJIT[j]):
        print(f"Oikein! +{OIKEA_PISTEET} pistettä.")
        print("Tiesitkö? " + FAKTAT[esine.laji])
        if pelaaja.oikein == YLENNYS_OIKEIN:
            if pelaaja.opas_luettu:
                print("Psst... olet lajitellut 5 roskaa oikein, nyt kannattaisi käydä pomon luona")
            else:
                print("Psst... olet lajitellut jo tarpeeksi. Pitäisiköhän sinun käydä taukohuoneessa kahvilla ja vaikka samalla käydä moikkaamassa uutta pomoasi hänen huoneessaan?")
    else:
        print(f"Väärin! -{VIRHE_PISTEET} pistettä. {esine.nimi} kuuluu kohtaan: {esine.laji}.")
    print(f"Nykyiset pisteesi: {pelaaja.pisteet}")
 
 
## Huoneen erikoistoiminto: taukohuoneessa luetaan opas, pomon huoneessa voi saada ylennyksen.
## Palauttaa "ylennys", jos peli päättyy ylennykseen, muuten None.
def huoneen_toiminto(pelaaja):
    toiminto = pelaaja.sijainti.toiminto
    if toiminto == "opas":
        if pelaaja.opas_luettu:
            print("Olet jo lukenut oppaan. Se auttaa sinua lajittelussa.")
        else:
            pelaaja.opas_luettu = True
            print("Luet kierrätysoppaan huolella. Jatkossa saat vinkin lajitellessasi.")
    elif toiminto == "pomo":
        if not pelaaja.opas_luettu:
            print("Pomo: No terve terve, käyppäs eka taukohuoneessa ennen tänne tulemista.")
        elif pelaaja.oikein < YLENNYS_OIKEIN:
            puuttuu = YLENNYS_OIKEIN - pelaaja.oikein
            print(f"Pomo: Hyvä, että olet lukenut oppaan! Lajittele vielä {puuttuu} esinettä oikein, niin saat ylennyksen!")
        else:
            return "ylennys"
    else:
        print("Täällä ei ole mitään tutkittavaa. Kokeile komentoja kerää ja lajittele.")
    return None
 
 
## Tarkistaa, onko peli voitettu tai hävitty. Jos ei, palauttaa None.
def tarkista_loppu(pelaaja):
    if pelaaja.pisteet >= VOITTOPISTEET:
        return "voitto"
    if pelaaja.pisteet <= 0:
        return "häviö"
    return None
 
 
## Tulostaa pelin lopetuksen ja poistaa tallennuksen
def näytä_loppu(pelaaja, loppu):
    print()
    if loppu == "voitto":
        print(f"{VOITTOPISTEET} pistettä! Pomo hymyilee ja onnittelee sinua: Lajittelit kaikki roskat oikein. Olet todellinen roskasankari!")
        print(f"Autoit luontoa ja edistit kestävää kehitystä kierrättämällä esineet oikein. Onnittelut voitosta, {pelaaja.nimi}!")
    elif loppu == "häviö":
        print("0 pistettä jäljellä: pomo käskee sinut huoneeseensa...")
        print("ja alkaa huutaamaan naama punaisena, niin, että tukkasi meinaa lähteä lentoon:")
        print("SINUT ON TÄLLÄ SEKUNILLA IRTISANOTTU JA TYÖSOPIMUKSESI PÄÄTTYY VÄLITTÖMÄSTI, HÄIVY SILMISTÄNI!")
    elif loppu == "ylennys":
        print("Pomo on vaikuttunut taidoistasi, lajittelit 5 roskaa oikein! Pomo ylentää sinut roskasankariksi!")
        print("Kiertelet nyt ylpeänä työpaikan käytävillä maski ja viitta päälläsi, työkaverisi kutsuvat sinua pomon lemppariksi.")
        print(f"Pisteesi: {pelaaja.pisteet}. Hienoa työtä, {pelaaja.nimi}!")
    poista_tallennus(pelaaja.nimi)

## Varmistaa sen, että pelaaja ei pysty pelaamaan tai käyttämään muita komentoja, ennen kuin hän on "aloittanut" pelin kirjoittamalla aluksi "aloita" 
def aloitusvalikko():
    print("Beep, boop, beep, beep...")
    time.sleep(2)
    print("Ohjelma käynnistyy, odota pieni hetki...")
    time.sleep(2)
    print("Ohjelma jäätyi, odota pieni hetki...")
    time.sleep(1)
    print("Tervetuloa Roskasankariin!")
    print("Komennot: aloita, lopeta")
    while True:
        komento = input("> ").strip().lower()
        if komento == "aloita":
            return True
        elif komento == "lopeta":
            return False
        else:
            print("Kirjoita aloita aloittaaksesi pelin tai 'lopeta' poistuaksesi ohjelmasta.")

## Pelin pääsilmukka
def pääohjelma():
    if not aloitusvalikko():
        print("Heippa!")    
        return
    print(lue_tiedosto("intro.txt"))
    print("Mikä nimesi on? ")
    nimi = input().strip()
    if nimi == "":
        nimi = "Tuntematon"
    huoneet = luo_huoneet()
 
    ## Jos nimellä löytyy tallennus, pelaaja voi jatkaa siitä
    pelaaja = None
    tallennus = lue_tallennus()
    if tallennus and tallennus["nimi"].lower() == nimi.lower():
        print("Löytyi tallennettu peli. Jatketaanko siitä? (kyllä/ei): ")
        vastaus = input()
        if vastaus.strip().lower() == "kyllä":
            pelaaja = lataa_peli(tallennus, huoneet)
 
    ## Uusi peli: kysytään ikä. Jatkettu peli: tervehditään pelaajaa.
    if pelaaja is None:
        ikä = kysy_ikä()
        if ikä < IKÄRAJA:
            print(f"Olet liian nuori pelaamaan tätä peliä, (ikäraja on: {IKÄRAJA} vuotta).")
            return
        pelaaja = Pelaaja(nimi, huoneet[0])
        print(f"Tervetuloa, {nimi}! Aloitat huoneesta: {pelaaja.sijainti.nimi}.")
    else:
        print(f"Tervetuloa takaisin, {pelaaja.nimi}! Pisteesi: {pelaaja.pisteet}.")
        
    print(lue_tiedosto("ohjeet.txt"))

    while True:
        print()
        print("<-------------------------------------- Päävalikko -------------------------------------->")
        print("Komennot: liiku, kerää, lajittele, tutki, esineet, pisteet, tallenna, ohje, lopeta")
        print(f"Nykyinen sijaintisi: {pelaaja.sijainti.nimi}  |  Pisteet: {pelaaja.pisteet}")
        print("<---------------------------------------------------------------------------------------->")
        print("Anna komento: ")
        komento = input().strip().lower()
        loppu = None
 
        if komento == "liiku":
            liiku_huoneeseen(pelaaja, huoneet)
        elif komento == "kerää":
            pelaaja.kerää_esine()
        elif komento == "lajittele":
            lajittele_roskat(pelaaja)
        elif komento == "tutki":
            loppu = huoneen_toiminto(pelaaja)
        elif komento == "esineet":
            näytä_esineet(pelaaja)
        elif komento == "pisteet":
            näytä_pisteet(pelaaja)
        elif komento == "tallenna":
            tallenna_peli(pelaaja)
            print("Peli tallennettu.")
        elif komento == "ohje":
            print(lue_tiedosto("ohjeet.txt"))
        elif komento == "lopeta":
            tallenna_peli(pelaaja)
            print("Peli tallennettu. Heippa,", pelaaja.nimi + "!")
            break
        else:
            print("Tuntematon komento. Yritä uudelleen.")
 
        ## Peli päättyy ylennykseen, voittoon tai häviöön
        if loppu is None:
            loppu = tarkista_loppu(pelaaja)
        if loppu is not None:
            näytä_loppu(pelaaja, loppu)
            break

pääohjelma()