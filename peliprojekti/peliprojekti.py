class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.sijainti = sijainti
        self.esineet = []

    def liiku(self, uusi_huone):
        self.sijainti = uusi_huone
        print(f"Siirryit uuteen huoneeseen: {uusi_huone.nimi}")

    def kerää_esine(self):
        if self.sijainti.esine is not None:
            esine = self.sijainti.esine
            self.esineet.append(esine)
            self.sijainti.esine = None
            print(f"Keräsit esineen: {esine.nimi}) (paino: {esine.paino} kg)")
        else: 
            print("Tässä huoneessa ei ole esineitä kerättäväksi.")

class Huone:
    def __init__(self, nimi, esine = None):
        self.nimi = nimi
        self.esine = esine

class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

lajittelupiste = Huone("Lajittelupiste", Esine("Cokispullo", 0.1))
pomon_huone = Huone("Pomon huone", Esine("Irtisanomissopimus", 0.05))
taukohuone = Huone("Taukohuone", None)

huoneet = [lajittelupiste, pomon_huone, taukohuone]

pelaaja = Pelaaja("Tico", lajittelupiste)

def aloita_peli(nimi):
    print("Peli alkaa! Onnea matkaan,", nimi + "!")

def liiku_huoneeseen(pelaaja, huoneet):
    print("Huoneet, joihin voit siirtyä:")
    for huone in huoneet:
        print("-", huone.nimi)
    kohde = input("Minne haluat siirtyä? ")

    löytyi = False
    for huone in huoneet:
        if huone.nimi.lower() == kohde.lower():
            pelaaja.liiku(huone)
            löytyi = True

    if not löytyi:
        print("Tuntematon huone.")

def näytä_esineet(pelaaja):
    if len(pelaaja.esineet) == 0:
        print("Reppusi on tyhjä.")
    else:
        print("Repussasi on seuraavat esineet:")
        for esine in pelaaja.esineet:
            print("-", esine.nimi, "(paino", str(esine.paino) + ")")

def näytä_pisteet():
    print("Sinulla ei ole vielä pisteitä. Pelaa ensin peliä!")

def näytä_ohje():
    print("Ohje: Kirjoita komentoja päävalikossa liikkuaksesi pelissä.")
    print("liiku  - siirry toiseen huoneeseen")
    print("kerää  - kerää esine nykyisestä huoneesta")

def lopeta_peli(nimi):
    print("Peli suljetaan. Näkemiin,", nimi + "!")

print("Mikä nimesi on?!")
nimi = input()
print("Minkä ikäinen olet?")
ikä = int(input())

if ikä >= 12:
    print("Olet", nimi, "ja olet", ikä, "vuotta vanha, joten saat pelata peliä.")
else:
    print("Voi ei, olet liian nuori pelaamaan tätä peliä! :(")

komento = ""
while komento != "lopeta":
    print()
    print("<----------------------- Päävalikko ---------------------->")
    print("<--------------------------------------------------------->")
    print("  Komennot: aloita, liiku, kerää, esineet, pisteet, ohje, lopeta")
    print("<--------------------------------------------------------->")
    komento = input("Anna komento: ")

    if komento == "aloita":
        aloita_peli(nimi)
    elif komento == "liiku":
        liiku_huoneeseen(pelaaja, huoneet)
    elif komento == "kerää":
        pelaaja.kerää_esine()
    elif komento == "esineet":
        näytä_esineet(pelaaja)
    elif komento == "pisteet":
        näytä_pisteet()
    elif komento == "ohje":
        näytä_ohje()
    elif komento == "lopeta":
        lopeta_peli(nimi)
    else:
        print("Tuntematon komento. Yritä uudelleen.")