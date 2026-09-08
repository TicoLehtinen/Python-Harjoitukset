def poista_parittomat(luvut):
    parilliset = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset

luvut = [3, 8, 5, 12, 7, 4, 9, 6]
tulos = poista_parittomat(luvut)

print("Alkuperäinen lista:", luvut)
print("Karsittu lista:", tulos)
