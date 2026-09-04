print("Mikä on biologinen sukupuolesi?")
sukupuoli = input()

print("Mikä on hemoglobiini arvosi, g/l?")
hemoglobiini = float(input())

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiinisi on liian alhainen")
    elif hemoglobiini <= 175:
        print("Hemoglobiinisi on normaali")
    else: print("Hemoglobiinisi on liian korkea")
                
if sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiinisi on liian alhainen")
    elif hemoglobiini <= 195:
        print("Hemoglobiinisi on normaali")
    else: print("Hemoglobiinisi on liian korkea")
