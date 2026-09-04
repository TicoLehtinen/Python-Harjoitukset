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
        print("---------- Päävalikko ----------")
        print("Komennot: aloita, pisteet, ohje, lopeta")
        print("---------------------------------")
        komento = input("Anna komento: ")

        if komento == "aloita":
            print("Peli alkaa! Onnea matkaan,", nimi + "!")
        elif komento == "pisteet":
            print("Sinulla ei ole vielä pisteitä. Pelaa ensin peliä!")
        elif komento == "ohje":
            print("Ohje: Kirjoita komentoja päävalikossa liikkuaksesi pelissä.")
        elif komento == "lopeta":
            print("Peli suljetaan. Näkemiin,", nimi + "!")
        else:
            print("Tuntematon komento. Yritä uudelleen.")

