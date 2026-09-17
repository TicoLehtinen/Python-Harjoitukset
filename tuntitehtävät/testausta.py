def pelaajan_elämä_pieni():
    print("Otit 10 pistettä vahinkoa!")
    return

def pelaajan_elämä_iso():
    print("Otit 30 pistettä vahinkoa!")
    return

print("Kuulet kamalan äänen ja huomaat, että sinua lähestyy hirvittävä hirviö!")
print("Hirviö on lohikäärme, joka hengittää tulta ja on erittäin vaarallinen.")
print("Mitä teet? (hyökkää, pakene, piiloudu")

pelaajan_valinta = input()

while pelaajan_valinta not in ("hyökkää", "pakene", "piiloudu"):
    print("Virheellinen valinta. Yritä uudelleen. (hyökkää, pakene, piiloudu)")
    pelaajan_valinta = input()
    
if pelaajan_valinta == "piiloudu":
    print("Onnistuit piiloutumaan ja löhikäärme ryntäsi ohitsesi huomaamatta sinua!")
elif pelaajan_valinta == "hyökkää":
    print("Hyökkäsit lohikäärmettä vastaan ja osuit, viiltäen lohikäärmeen suomuja miekallasi. Lohikäärme suuttui tästä ja läimäisi sinua hännällään, jonka johdosta lensit päin seinää")
    pelaajan_elämä_iso()
elif pelaajan_valinta == "pakene":
    print("Yritit paeta lohikäärmettä, mutta olit liian hidas ja sen tulinen henkäys osui sinuun, vahingoittaen sinua")
    pelaajan_elämä_pieni()
