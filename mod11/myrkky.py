class Potion:
    def __init__(self, nimi):
        self.nimi = nimi

class Parannusjuoma(Potion):
    def __init__(self, nimi, hp):
        super().__init__(nimi)
        self.hp = hp

juoma = Parannusjuoma("Terveysjuoma",2)
print(f"{juoma.nimi}: + {juoma.hp}")

class Myrkky(Potion):
    def __init__(self, nimi, hp, määrä):
        super().__init__(nimi)
        self.hp = hp
        self.määrä = määrä

juoma = Parannusjuoma("Terveysjuoma",2)
print(f"{juoma.nimi}: + {juoma.hp}")
myrkky = Myrkky("Örkintappaja", 5, 3)
print(f"{myrkky.nimi}: - {myrkky.hp}, jäljellä: {myrkky.määrä}")

    