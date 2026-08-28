print("Kirjoita luku")
luku = int(input())

pienin = None
suurin = None

while luku != "":
    luku = float(luku)
    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku
    print("Kirjoita luku")
    luku = input()

print("Pienin:", pienin)
print("Suurin:", suurin)



