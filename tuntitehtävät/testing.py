class Auto:
    def __init__(self, merkki, malli, vuosimalli):
        self.merkki = merkki
        self.malli = malli
        self.vuosimalli = vuosimalli
        
Sähköauto1 = Auto("Tesla", "Model S", 2023)
Sähköauto2 = Auto("Lucid", "Air", 2025)

print("Valitse auto")
auto = input()

if auto == Sähköauto1.merkki:
    print(f"Auton merkki on: {Sähköauto1.merkki}, auton malli on: {Sähköauto1.malli} ja sen vuosimalli on: {Sähköauto1.vuosimalli}")
elif auto == Sähköauto2.merkki:
        print(f"Auton merkki on: {Sähköauto2.merkki}, auton malli on: {Sähköauto2.malli} ja sen vuosimalli on: {Sähköauto2.vuosimalli}")
    
    