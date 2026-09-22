class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}, Kirjan kirjoittaja on: {self.kirjoittaja}, Kirjan sivumäärä on: {self.sivumäärä}")
    
class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja
    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}, Lehden päätoimittaja on: {self.päätoimittaja}")
        

lehti = Lehti("Aku Ankka", "Aki Hyyppä")

kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()
    
