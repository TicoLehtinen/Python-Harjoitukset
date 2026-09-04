print("Anna käyttäjätunnus")
käyttäjätunnus = input()

print("Anna salasana")
salasana = input()

while käyttäjätunnus != "python" or salasana != "rules":
    print("Käyttäjätunnus tai salasana on väärin, yritä uudelleen")
    print("Anna käyttäjätunnus")
    käyttäjätunnus = input()
    print("Anna salasana")
    salasana = input()
else:
    print("Tervetuloa")
