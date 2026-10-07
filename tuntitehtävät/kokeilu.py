class Opiskelija:
    def __init__(self, kurssit, nimi, opiskelijanumero):
        self.kurssit = kurssit
        self.nimi = nimi
        self.opiskelijanumero = opiskelijanumero
        
class Kurssi:
    def __init__(self, opiskelijat, nimi, opintopisteidenmäärä):
        self.opiskelijat = opiskelijat
        self.nimi = nimi
        self.opintopisteidenmäärä = opintopisteidenmäärä
    
    
opiskelija1 = Opiskelija(["Matematiikka", "Viestintä", "Fysiikka"], "Markus", 123)

kurssi1 = Kurssi(["Markus", "Janne", "Miikka", "Sofia"], "Ohjelmointi1", 5)

print("Opiskelijan kurssit:", (opiskelija1.kurssit))
print("Opiskelijan nimi:", opiskelija1.nimi)
print("Opiskelijan opiskelijanumero", opiskelija1.opiskelijanumero)

print("Kurssilla olevat opiskelijat:", kurssi1.opiskelijat)
print("Kurssin nimi:", kurssi1.nimi)
print("Kurssin opintopisteiden määrä:", kurssi1.opintopisteidenmäärä)

print("Kurssilla on opiskelijoita:")
print(len(kurssi1.opiskelijat))



monikko1 = 1, 2, 3, 4, 5
print(monikko1[-1:-0])