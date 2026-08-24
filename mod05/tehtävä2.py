print("Kirjoita tuumamäärä")
tuuma = float(input())

while tuuma >= 0:
    senttimetriä = tuuma * 2.54
    print(f"{tuuma} tuumaa on {senttimetriä} senttimetria")
    tuuma = float(input())

print("Ohjelma lopetettu.")