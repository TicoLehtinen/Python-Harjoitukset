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


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(huippunopeus, rekisteritunnus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankinkoko):
        super().__init__(huippunopeus, rekisteritunnus)
        self.bensatankinkoko = bensatankinkoko


sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdytä(120)
polttomoottoriauto.kiihdytä(100)

sähköauto.kulje(3)
polttomoottoriauto.kulje(3)

print(f"Sähköauton {sähköauto.rekisteritunnus} matkamittarilukema: {sähköauto.kuljettu_matka} km")
print(f"Polttomoottoriauton {polttomoottoriauto.rekisteritunnus} matkamittarilukema: {polttomoottoriauto.kuljettu_matka} km")