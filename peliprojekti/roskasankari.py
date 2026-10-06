import os
import random

# ---------- Asetukset ----------
KANSIO = os.path.dirname(os.path.abspath(__file__))
TALLENNUSTIEDOSTO = os.path.join(KANSIO, "tallennus.txt")
IKÄRAJA = 12
ALKUPISTEET = 20
VOITTOPISTEET = 100
OIKEA_PISTEET = 10
VIRHE_PISTEET = 5
REPUN_RAJA = 1.0
YLENNYS_OIKEIN = 5

LAJIT = ["muovi", "lasi", "paperi", "metalli", "biojäte", "sekajäte"]

## Roskat, joita pelaaja voi kerätä ja lajitella: nimi, paino ja oikea laji.
ROSKAT = [
    ("Cokispullo", 0.1, "muovi"),
    ("Muovipussi", 0.05, "muovi"),
    ("Shampoopullo", 0.15, "muovi"),
    ("Lasipullo", 0.4, "lasi"),
    ("Lasiastia", 0.3, "lasi"),
    ("Sanomalehti", 0.3, "paperi"),
    ("Maitopurkki", 0.1, "paperi"),
    ("Säilyketölkki", 0.2, "metalli"),
    ("Juomatölkki", 0.05, "metalli"),
    ("Banaaninkuori", 0.15, "biojäte"),
    ("Puoliksi syöty omena", 0.1, "biojäte"),
    ("Rikkinäinen kahvikuppi", 0.25, "sekajäte"),
]

## Faktat, jotka pelaajalle näytetään, kun roska lajitellaan oikein.
FAKTAT = {
    "muovi": "Kierrätetystä muovista voidaan tehdä uusia tuotteita, esim. polyester vaatteita.",
    "lasi": "Lasi voidaan kierrättää uudelleen ja uudelleen.",
    "paperi": "Kierrätyspaperi säästää raaka-aineita ja energiaa.",
    "metalli": "Metallin kierrätys säästää paljon energiaa uuden valmistamiseen verrattuna.",
    "biojäte": "Biojätteestä voidaan tehdä biokaasua ja multaa.",
    "sekajäte": "Mitä paremmin lajittelet, sitä vähemmän jätettä päätyy poltettavaksi.",
}


## Esine luokka
class Esine:
    def __init__(self, nimi, paino, laji):
        self.nimi = nimi
        self.paino = paino
        self.laji = laji


## Huone luokka
class Huone:
    def __init__(self, nimi, kuvaus, tuottaa_roskaa=False, toiminto=None):
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.esine = None
        self.tuottaa_roskaa = tuottaa_roskaa
        self.toiminto = toiminto

    ## Arpoo uuden roskan huoneeseen, jos huoneessa pystyy tekemään niin (Lajittelupiste!).
    def täydennä(self):
        if self.tuottaa_roskaa and self.esine is None:
            nimi, paino, laji = random.choice(ROSKAT)
            self.esine = Esine(nimi, paino, laji)


## Pelaaja luokka
class Pelaaja:
    def __init__(self, nimi, ikä, sijainti):
        self.nimi = nimi
        self.ikä = ikä
        self.sijainti = sijainti
        self.esineet = []
        self.pisteet = ALKUPISTEET
        self.oikein = 0  # oikeat lajittelut yhteensä
        self.opas_luettu = False  # onko kierrätysopas luettu

    def liiku(self, uusi_huone):
        self.sijainti = uusi_huone
        uusi_huone.täydennä()
        print(f"Siirryit uuteen huoneeseen: {uusi_huone.nimi}")
        print(uusi_huone.kuvaus)

    def repun_paino(self):
        return round(sum(esine.paino for esine in self.esineet), 2)

    def kerää_esine(self):
        esine = self.sijainti.esine
        if esine is None:
            print("Tässä huoneessa ei ole esineitä kerättäväksi.")
        elif self.repun_paino() + esine.paino > REPUN_RAJA:
            print(f"Reppu on liian painava! Lajittele ensin (raja {REPUN_RAJA} kg).")
        else:
            self.esineet.append(esine)
            self.sijainti.esine = None
            self.sijainti.täydennä()
            print(f"Keräsit esineen: {esine.nimi} (paino: {esine.paino} kg)")

    ## Lajittelee esineen ja palauttaa True, jos laji oli oikea, muuten False.
    def lajittele(self, esine, laji):
        self.esineet.remove(esine)
        if esine.laji == laji:
            self.pisteet += OIKEA_PISTEET
            self.oikein += 1
            return True
        self.pisteet = max(0, self.pisteet - VIRHE_PISTEET)
        return False


## Lukee tekstitiedoston (intro.txt tai ohjeet.txt) ja palauttaa sen tekstin.
def lue_tiedosto(tiedostonimi):
    try:
        with open(os.path.join(KANSIO, tiedostonimi), "r", encoding="utf-8") as t:
            return t.read()
    except FileNotFoundError:
        return f"(Tiedostoa {tiedostonimi} ei löytynyt.)"


## Tallentaa pelitilanteen tiedostoon yhdelle riville. Reppu tallennetaan esineiden nimillä.
def tallenna_peli(pelaaja):
    reppu = ",".join(esine.nimi for esine in pelaaja.esineet)
    osat = [
        pelaaja.nimi,
        str(pelaaja.ikä),
        str(pelaaja.pisteet),
        str(pelaaja.oikein),
        "1" if pelaaja.opas_luettu else "0",
        pelaaja.sijainti.nimi,
        reppu,
    ]
    with open(TALLENNUSTIEDOSTO, "w", encoding="utf-8") as tiedosto:
        tiedosto.write(";".join(osat))


## Lukee tallennuksen ja palauttaa sen kentät listana. Jos tallennusta ei ole, palauttaa None.
def lue_tallennus():
    try:
        with open(TALLENNUSTIEDOSTO, "r", encoding="utf-8") as tiedosto:
            return tiedosto.read().strip().split(";")
    except FileNotFoundError:
        return None


## Tekee tallennuksen kentistä (osat) takaisin Pelaaja-olion.
def lataa_peli(osat, huoneet):
    try:
        sijainti = huoneet[0]
        for huone in huoneet:
            if huone.nimi == osat[5]:
                sijainti = huone
        pelaaja = Pelaaja(osat[0], int(osat[1]), sijainti)
        pelaaja.pisteet = int(osat[2])
        pelaaja.oikein = int(osat[3])
        pelaaja.opas_luettu = osat[4] == "1"
        for esineen_nimi in osat[6].split(","):
            for nimi, paino, laji in ROSKAT:
                if nimi == esineen_nimi:
                    pelaaja.esineet.append(Esine(nimi, paino, laji))
        return pelaaja
    except (ValueError, IndexError):
        print("Tallennus oli rikkoutunut, aloitetaan uusi peli.")
        return None


## Poistaa tallennuksen, kun peli on päättynyt (sitä ei voi enää jatkaa).
def poista_tallennus(nimi):
    osat = lue_tallennus()
    if osat and osat[0].lower() == nimi.lower():
        os.remove(TALLENNUSTIEDOSTO)


## Kysyy iän, kunnes pelaaja antaa kelvollisen numeron.
def kysy_ikä():
    while True:
        try:
            ikä = int(input("Minkä ikäinen olet? "))
            if 0 < ikä < 120:
                return ikä
        except ValueError:
            pass
        print("Anna ikä numerona, esim. 12.")


## Luo huoneet ja palauttaa ne listana. Ensimmäinen huone on aloitushuone.
def luo_huoneet():
    lajittelupiste = Huone(
        "Lajittelupiste",
        "Täällä ovat roskikset ja roskia tulee jatkuvasti lisää.",
        tuottaa_roskaa=True,
    )
    lajittelupiste.esine = Esine("Cokispullo", 0.1, "muovi")
    pomon_huone = Huone(
        "Pomon huone",
        "Pomo katsoo sinua tiukasti silmiin. Hänen kanssaan voi keskustella (tutki).",
        toiminto="pomo",
    )
    taukohuone = Huone(
        "Taukohuone",
        "Kahvinkeitin porisee kuumana. Pöydällä näyttäisi olevan jokin lappu (tutki).",
        toiminto="opas",
    )
    return [lajittelupiste, pomon_huone, taukohuone]


## Tulostaa vaihtoehdot numeroituna ja palauttaa valitun indeksin (None, jos valinta ei ole olemassa).
def valitse_listasta(kysymys, vaihtoehdot):
    for numero, vaihtoehto in enumerate(vaihtoehdot, 1):
        print(f"  {numero}. {vaihtoehto}")
    vastaus = input(kysymys).strip()
    if vastaus.isdigit() and 1 <= int(vastaus) <= len(vaihtoehdot):
        return int(vastaus) - 1
    return None


## Liikuttaa pelaajaa valittuun huoneeseen. Printtaa listan huoneista, joita pelissä on.
def liiku_huoneeseen(pelaaja, huoneet):
    print("Huoneet, joihin voit siirtyä:")
    i = valitse_listasta("Minne haluat siirtyä? (numero) ", [h.nimi for h in huoneet])
    if i is None:
        print("Tuntematon huone.")
    else:
        pelaaja.liiku(huoneet[i])


## Printtaa pelaajan repussa olevat esineet ja niiden painon. Jos reppu on tyhjä, sekin tulostetaan.
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


## Pelaaja valitsee repusta esineen ja roskiksen, johon esine lajitellaan. Pisteet päivittyvät.
def lajittele_roskat(pelaaja):
    if pelaaja.sijainti.nimi != "Lajittelupiste":
        print("Roskikset ovat Lajittelupisteessä. Mene sinne ensin.")
        return
    if len(pelaaja.esineet) == 0:
        print("Reppusi on tyhjä. Kerää ensin jotain lajiteltavaa.")
        return

    print("Mikä esine lajitellaan?")
    i = valitse_listasta("Valinta (numero): ", [e.nimi for e in pelaaja.esineet])
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
        print("Tiesitkö? " + FAKTAT[LAJIT[j]])
    else:
        print(
            f"Väärin! -{VIRHE_PISTEET} pistettä. {esine.nimi} kuuluu kohtaan: {esine.laji}."
        )
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
            print("Pomo: 'Käy ensin lukemassa kierrätysopas taukohuoneessa.'")
        elif pelaaja.oikein < YLENNYS_OIKEIN:
            puuttuu = YLENNYS_OIKEIN - pelaaja.oikein
            print(
                f"Pomo: 'Hyvä, että olet lukenut oppaan! Lajittele vielä {puuttuu} esinettä oikein.'"
            )
        else:
            return "ylennys"
    else:
        print("Täällä ei ole mitään tutkittavaa. Kokeile komentoja kerää ja lajittele.")
    return None


## Tarkistaa, onko peli voitettu tai hävitty. Jos ei, palauttaa None ja peli jatkuu.
def tarkista_loppu(pelaaja):
    if pelaaja.pisteet >= VOITTOPISTEET:
        return "voitto"
    if pelaaja.pisteet <= 0:
        return "häviö"
    return None


## Tulostaa pelin lopetuksen ja poistaa tallennuksen.
def näytä_loppu(pelaaja, loppu):
    print()
    if loppu == "voitto":
        print(
            f"LOPPU 1: {VOITTOPISTEET} pistettä! Pomo hymyilee: 'Olet paras lajittelija ikinä!'"
        )
        print(
            "Autoit luontoa ja kierrätit esineet onnistuneesti. Onnittelut voitosta, "
            + pelaaja.nimi
            + "!"
        )
    elif loppu == "häviö":
        print("LOPPU 2: 0 pistettä jäljellä: pomo käskee sinut huoneeseensa...")
        print(
            "ja alkaa huutaamaan naama punaisena, niin, että tukkasi meinaa lähteä lentoon:"
        )
        print(
            "SINUT ON TÄLLÄ SEKUNILLA IRTISANOTTU JA TYÖSOPIMUKSESI PÄÄTTYY VÄLITTÖMÄSTI, HÄIVY SILMISTÄNI!"
        )
    elif loppu == "ylennys":
        print(
            "LOPPU 3: Pomo vaikuttuu taidoistasi ja ylentää sinut kierrätysneuvojaksi!"
        )
        print(
            "Kiertelet nyt ylpeänä työpaikan käytävillä ja työkaverisi kutsuvat sinua pomon lemppariksi."
        )
        print(f"Pisteesi: {pelaaja.pisteet}. Hienoa työtä, {pelaaja.nimi}!")
    poista_tallennus(pelaaja.nimi)


## Pelin pääsilmukka. Kysyy ja näyttää komentoja, kunnes peli päättyy tai pelaaja lopettaa pelin.
def main():
    print(lue_tiedosto("intro.txt"))
    print(lue_tiedosto("ohjeet.txt"))
    nimi = input("Mikä nimesi on? ").strip().replace(";", "") or "Tuntematon"
    huoneet = luo_huoneet()

    ## Jos nimellä löytyy tallennus, pelaaja voi jatkaa siitä.
    pelaaja = None
    tallennus = lue_tallennus()
    if tallennus and tallennus[0].lower() == nimi.lower():
        vastaus = input("Löytyi tallennettu peli. Jatketaanko siitä? (kyllä/ei): ")
        if vastaus.strip().lower() == "kyllä":
            pelaaja = lataa_peli(tallennus, huoneet)

    ## Jos käyttäjän antamaa nimeä ei löydy, niin peli "alkaa" alusta ja kysytään ikä.
    ## Jos pelaajan tiedot löytyvät, niin peli jatkuu siitä mihin jäätiin ja peli tervehtii pelaajaa ja kertoo pisteet.
    if pelaaja is None:
        ikä = kysy_ikä()
        if ikä < IKÄRAJA:
            print(
                f"Olet liian nuori pelaamaan tätä peliä, (ikäraja on: {IKÄRAJA} vuotta)."
            )
            return
        pelaaja = Pelaaja(nimi, ikä, huoneet[0])
        print(f"Tervetuloa, {nimi}! Aloitat huoneesta: {pelaaja.sijainti.nimi}.")
    else:
        pelaaja.sijainti.täydennä()
        print(f"Tervetuloa takaisin, {pelaaja.nimi}! Pisteesi: {pelaaja.pisteet}.")

    komento = ""
    while komento != "lopeta":
        print()
        print(
            "<-------------------------------------- Päävalikko -------------------------------------->"
        )
        print(
            "Komennot: liiku, kerää, lajittele, tutki, esineet, pisteet, tallenna, ohje, lopeta"
        )
        print(
            f"Nykyinen sijaintisi: {pelaaja.sijainti.nimi}  |  Pisteet: {pelaaja.pisteet}"
        )
        print(
            "<---------------------------------------------------------------------------------------->"
        )
        komento = input("Anna komento: ").strip().lower()
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
        else:
            print("Tuntematon komento. Yritä uudelleen.")

        ## Peli päättyy ylennykseen, (jos pomon huoneessa käydään ja käytetään tutki-komentoa) voittoon tai häviöön.
        if loppu is None:
            loppu = tarkista_loppu(pelaaja)
        if loppu is not None:
            näytä_loppu(pelaaja, loppu)
            break


if __name__ == "__main__":
    main()
