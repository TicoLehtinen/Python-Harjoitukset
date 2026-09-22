class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        print("Hissi on kerroksessa", self.nykyinen_kerros)

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print("Hissi on kerroksessa", self.nykyinen_kerros)

    def siirry_kerrokseen(self, kerros):
        while self.nykyinen_kerros < kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kerros:
            self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissien_määrä):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(hissien_määrä):
            self.hissit.append(Hissi(alin, ylin))

    def käytä_hissiä(self, hissin_numero, kerros):
        self.hissit(hissien_määrä).siirry_kerrokseen(kerros)


talot = Talo(1, 10, 3)
print("")

talot.käytä_hissiä(2, 4)


h = Hissi(0, 5)
print("Hissi on kerroksessa", h.nykyinen_kerros)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(h.alin_kerros)
