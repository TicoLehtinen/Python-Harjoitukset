import random 

print("Anna arpakuutioiden määrä")
määrä = int(input())
    
summa = 0
for i in range(määrä):
    silmäluku = random.randint(1, 6)                               
    summa += silmäluku

print("Silmälukujen summa on:", summa)