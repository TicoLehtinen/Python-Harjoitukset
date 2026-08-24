print("Kirjoita luku")
kirjoitus = input()

pienin = None
suurin = None

while kirjoitus != "":
    luku = float(kirjoitus)

    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku

    kirjoitus = input()


print("Pienin luku:", pienin)
print("Suurin luku:", suurin)