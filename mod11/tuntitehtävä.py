class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
        self.onko_lainassa = False

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        lainassa = "Kyllä" if self.onko_lainassa else "Saatavilla hyllystä"
        return (f"Kirja: {self.nimi}, Kirjan kirjoittaja on: {self.kirjoittaja}, "
                f"Kirjan sivumäärä on: {self.sivumäärä}, Lainassa: {lainassa}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        lainassa = "Kyllä" if self.onko_lainassa else "Saatavilla hyllystä"
        return (f"Lehti: {self.nimi}, Lehden päätoimittaja on: {self.päätoimittaja}, "
                f"Lainassa: {lainassa}")


lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

kirja.onko_lainassa = True

julkaisut = [lehti, kirja]

with open("kirjasto.txt", "w") as tiedosto:
    for julkaisu in julkaisut:
        rivi = julkaisu.tulosta_tiedot()
        print(rivi)
        tiedosto.write(rivi + "\n")