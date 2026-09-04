print("Maria oli rohkea ritari, joka joutui kaksintaisteluun. Minkä aseen Maria ottaa?")
ase = input()

while ase != "miekka":
    if ase == "tikari":
        print("Huono valinta, valitse toinen ase")
    elif ase == "nuija":
        print("Huono valinta, valitse toinen ase")
    else:
        print("Tuntematon ase, valitse toinen ase")
    ase = input()

print("Maria valitsi miekan ja voitti kaksintaistelun!")
