class Pankkitili:
    def __init__(self, tilinomistaja, saldo=0):
        self.tilinomistaja = tilinomistaja
        self.saldo = saldo

    def talleta(self, määrä):
        if määrä > 0:
            self.saldo += määrä

    def nosta(self, määrä):
        if määrä <= self.saldo:
            määrä -= self.saldo

print("Tervetuloa automaatille, haluatko nostaa vai tallettaa rahaa?")
valinta = input()

if valinta == "nosta":
    print("Kuinka paljon haluat nostaa rahaa?")

määrä = int(input())

elif määrä <= self.saldo:
nosta()







