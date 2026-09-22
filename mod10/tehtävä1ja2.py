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
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissin_numero, kerros):
        self.hissit[hissin_numero].siirry_kerrokseen(kerros)
        
print("Yksittäisen hissin testaus:")
h = Hissi(0, 10)
print("Hissi on kerroksessa", h.nykyinen_kerros)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(h.alin_kerros)

print()

print("Talon hissien testaus:")
talo = Talo(0, 10, 3)

talo.aja_hissiä(0, 4)
talo.aja_hissiä(1, 7)
talo.aja_hissiä(2, 2)