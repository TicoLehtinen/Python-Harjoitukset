print("Mitä lajia olet?")
laji = input()
print("Minkä ikäinen olet?")
ikä = int(input())

print("Minkä juoman haluaisit tilata: kahvi, viini, olut vai öljy?")
juoma = input()

if juoma == "kahvi" and (laji == "ihminen" or "tonttu" or "robotti"):
    print("Tässä kahvisi, ole hyvä!")
elif juoma == "viini" and laji == "ihminen" and ikä >= 18:
    print("Tässä viinisi, ole hyvä")
elif juoma == "olut" and laji == "tonttu" and ikä >= 100:
    print("Tässä oluesi, ole hyvä!")
elif juoma == "öljy" and laji == "robotti":
    print("Tässä öljysi, ole hyvä!")

else:
    print("Et voi tilata tätä juomaa, sillä se ei kuulu sinun lajillesi")
