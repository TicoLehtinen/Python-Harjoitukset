def averages(luvut):
    return sum(luvut) / len(luvut)


luvut = []

print("Anna luku")
syöte = input()

while syöte != "":
    luku = float(syöte)
    luvut.append(luku)
    print("Anna luku")
    syöte = input()

if len(luvut) == 0:
    print("Et antanut yhtään lukua")
else:
    print("Keskiarvo on,", averages(luvut))
