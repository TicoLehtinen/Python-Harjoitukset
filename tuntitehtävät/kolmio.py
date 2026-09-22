print("Anna korkeus")
korkeus = int(input())

for i in range(1, korkeus + 1):
    valilyonnit = " " * (korkeus - i)
    tahdet = "*" * (2 * i - 1)
    print(valilyonnit + tahdet)