print("Anna vuosiluku")
vuosiluku = int(input())

while vuosiluku >= 1896:
    if vuosiluku % 4 == 0:
        print("Vuosi on olympiavuosi")
    elif vuosiluku == 2020:
        print("Olympialaiset järjestettiin poikkeuksellisesti vuonna 2021")
    else:
        print("Vuosi ei ole olympiavuosi")
    vuosiluku = int(input("Anna uusi vuosiluku: "))

print("Vuosi on ennen moderneja olympialaisia (1896)")