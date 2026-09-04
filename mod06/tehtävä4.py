kaupungit = []

for i in range(5):
    kaupunki = input("Anna kaupungin nimi: ")
    kaupungit.append(kaupunki)

print("\nSyöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)