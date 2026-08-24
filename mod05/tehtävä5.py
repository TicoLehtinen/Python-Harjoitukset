print("Anna käyttäjätunnus")
käyttäjätunnus = input()
print("Anna salasana")
salasana = input()

yritykset = 1

while käyttäjätunnus != "python" or salasana != "rules":
    yritykset += 1
    if yritykset > 5:
        print("Pääsy evätty")
        break
    print("Väärä käyttäjätunnus tai salasana")
    print("Kirjoita käyttäjätunnus ja salasana uudestaan")
    käyttäjätunnus = input()
    print("Anna salasana")
    salasana = input()
else:
    print("Tervetuloa!")