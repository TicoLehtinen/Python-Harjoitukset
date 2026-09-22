import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self):
        muutos = random.randint(-10, 15)
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self):
        self.matka += self.nopeus

    def __str__(self):
        return (f"{self.rekisteritunnus:8s}"
                f"huippunopeus: {self.huippunopeus:3d} km/h   "
                f"nopeus: {self.nopeus:3d} km/h   "
                f"matka: {self.matka:6d} km")

class Kilpailu:
    def __init__(self, nimi, kilometrit, autot):
        self.nimi = nimi
        self.kilometrit = kilometrit
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdytä()
        for auto in self.autot:
            auto.kulje()

    def tulosta_tilanne(self):
        print(f"--- {self.nimi}, tilanne ---")
        for auto in self.autot:
            print(auto)
        print()

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.kilometrit:
                return True
        return False

autot = []
for i in range(1, 11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunteja = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunteja += 1
    if tunteja % 10 == 0:
        print(f"({tunteja} tuntia kulunut)")
        kilpailu.tulosta_tilanne()

print(f"Kilpailu ohi {tunteja} tunnin jälkeen!")
kilpailu.tulosta_tilanne()