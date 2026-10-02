import harjoitus1

print("Anna numero")
arvo = float(input())

if harjoitus1.is_empty(arvo):
    print("Tyhjä")
elif harjoitus1.is_number(arvo):
    print("Voidaan muuttaa numeroksi")

else:
    print("Ei ole numero")
