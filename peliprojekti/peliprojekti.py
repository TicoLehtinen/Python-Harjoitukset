reppu = []

def aloita_peli(nimi):
    print("Peli alkaa! Onnea matkaan,", nimi + "!")

def lisää_esine(reppu):
    esine = input("Minkä esineen haluat lisätä reppuun? ")
    reppu.append(esine)
    print("Reppuusi lisättiiin 1 kpl:", esine)

def näytä_esineet(reppu):
    if len(reppu) == 0:
        print("Reppusi on tyhjä.")
    else:
        print("Repussasi on seuraavat esineet:")
        for esine in reppu:
            print("-", esine)

def näytä_pisteet():
    print("Sinulla ei ole vielä pisteitä. Pelaa ensin peliä!")

def näytä_ohje():
    print("Ohje: Kirjoita komentoja päävalikossa liikkuaksesi pelissä.")

def lopeta_peli(nimi):
    print("Peli suljetaan. Näkemiin,", nimi + "!")


print("Mikä nimesi on?!")
nimi = input()
print("Minkä ikäinen olet?")
ikä = int(input())

if ikä >= 12:
    print("Olet", nimi, "ja olet", ikä, "vuotta vanha, joten saat pelata peliä.")
else:
    print("Voi ei, olet liian nuori pelaamaan tätä peliä! :(")

komento = ""
while komento != "lopeta":
    print()
    print("<----------------------- Päävalikko ---------------------->")
    print("<--------------------------------------------------------->")
    print("  Komennot: aloita, lisää, esineet, pisteet, ohje, lopeta")
    print("<--------------------------------------------------------->")
    komento = input("Anna komento: ")

    if komento == "aloita":
        aloita_peli(nimi)
    elif komento == "lisää":
        lisää_esine(reppu)
    elif komento == "esineet":
        näytä_esineet(reppu)
    elif komento == "pisteet":
        näytä_pisteet()
    elif komento == "ohje":
        näytä_ohje()
    elif komento == "lopeta":
        lopeta_peli(nimi)
    else:
        print("Tuntematon komento. Yritä uudelleen.")

