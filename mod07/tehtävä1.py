import random

def heitä_noppaa():
    return random.randint(1, 6)

silmäluku = heitä_noppaa()
print("Heitit:", silmäluku)

while silmäluku != 6:
    silmäluku = heitä_noppaa()
    print("Heitit:", silmäluku)