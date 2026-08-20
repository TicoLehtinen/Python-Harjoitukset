
pituus =float (input("Kuinka pitkä kuha on?"))
maksimi = 37
if pituus < 37:
    erotus = maksimi - pituus
    print("Kuha on", erotus, "cm liian lyhyt, päästä se takaisin veteen.")
if pituus >=37:
    print("Kuha on tarpeeksi iso, onnea saaliista!") 
