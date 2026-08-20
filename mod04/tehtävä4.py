print("Kirjoita vuosiluku")
vuosiluku = float(input())
if vuosiluku % 4 == 0 and (vuosiluku % 100 != 0 or vuosiluku % 400 == 0):
    print("Vuosi on karkausvuosi")
else: print("Vuosi ei ole karkausvuosi")
