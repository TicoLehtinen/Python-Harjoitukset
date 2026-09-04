numerot = []

print("Anna luku")
luku = input()

while luku != "":
    numerot.append(float(luku))
    print("Anna luku tai lopeta painamalla enter")
    luku = input()

numerot.sort(reverse=True)

print("Viisi suurinta lukua:")
for luku in numerot[:5]:
    print(luku)
