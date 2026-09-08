import random

def heitä_noppaa(tahkojen_määrä):
    return random.randint(1, tahkojen_määrä)

tahkojen_määrä = int(input("Anna nopan tahkojen määrä: "))

silmäluku = heitä_noppaa(tahkojen_määrä)
print("Heitit:", silmäluku)

while silmäluku != tahkojen_määrä:
    silmäluku = heitä_noppaa(tahkojen_määrä)
    print("Heitit:", silmäluku)