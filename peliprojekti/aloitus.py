print("Mikä nimesi on?!")
nimi = input()
print("Minkä ikäinen olet?")
ikä = int(input())
if ikä >= 12:
    print("Nimesi on", nimi, "ja olet", ikä, "vuotta vanha.")
else: print("Voi ei, olet liian nuori pelaamaan tätä peliä! :(")
