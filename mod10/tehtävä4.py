import random

class Auto:

    def __init__(self, huippunopeus, rekisteritunnus):
        self.huippunopeus = huippunopeus
        self.rekisteritunnus = rekisteritunnus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, nopeuden_muutos):
        uusi_nopeus = self.tämänhetkinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tämänhetkinen_nopeus = 0
        else:
            self.tämänhetkinen_nopeus = uusi_nopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.tämänhetkinen_nopeus * tunnit


autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    uusi_auto = Auto(huippunopeus, rekisteritunnus)
    autot.append(uusi_auto)

kilpailu_käynnissä = True
kuluneet_tunnit = 0

while kilpailu_käynnissä:
    kuluneet_tunnit += 1

    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)
        auto.kulje(1)

        if auto.kuljettu_matka > 1000:
            kilpailu_käynnissä = False
            break

print(f"Kilpailu päättyi! Aikaa kului {kuluneet_tunnit} tuntia.\n")
print(f"{'Rekkari':<12} | {'Huippunopeus':<15} | {'Nopeus (km/h)':<15} | {'Matka (km)':<12}")

for auto in autot:
    print(f"{auto.rekisteritunnus:<12} | {auto.huippunopeus:<15} | {auto.tämänhetkinen_nopeus:<15} | {auto.kuljettu_matka:<12}")


class Kilpailu:
    def __init__(self, kilpailunnimi, pituuskilometreinä, osallistuvienautojenlista):
        self.kilpailunnimi = kilpailun_nimi
        self.pituuskilometreinä = pituus_kilometreinä
        self. osallistuvienautojenlista = []
        
        
    def tunti_kuluu(self):
        
    def tulosta_tilanne(self):
        
    def kilpailu_ohi(self):
        