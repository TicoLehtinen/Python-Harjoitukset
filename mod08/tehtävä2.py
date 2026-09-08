nimet = set()

print("Anna nimi (tyhjä lopettaa):")
nimi = input()

while nimi != "":
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)
    print("Anna nimi (tyhjä lopettaa):")
    nimi = input()
    

print("\nSyötetyt nimet:")
for n in nimet:
    print(n)