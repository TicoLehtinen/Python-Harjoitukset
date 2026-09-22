class Potion:
    def __init__(self, nimi):
        self.nimi = nimi

    def kayta(self):
        print(f"Käytät potionin")

class Parannusjuoma(Potion):
    def __init__(self, nimi, hp):
        super().__init__(nimi)
        self.hp = hp

    def kayta(self):
        super().kayta()
        return self.hp



juoma = Parannusjuoma("Terveysjuoma",2)
parannus = juoma.kayta()
print(f"Parannut {parannus} pistettä ")

