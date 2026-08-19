## 6. Tehtävä

import random

koodi = [random.randint(0, 9) for _ in range(3)]
print("Haluatko kolminumeroisen koodin, kyllä vai ei?")
if input() == "kyllä": 
    print("ok, tässä sulle koodi! : ) ")
    print (*koodi)
else: print("ok, et vissiin tarvii koodia sitten : ( ")




import random

koodi = [random.randint(1, 6) for _ in range(4)]
print("Haluatko nelinumeroisen koodin, kyllä vai ei?")
if input() == "kyllä": 
    print("ok, tässä sulle koodi! : )")
    print (*koodi)
else: print("ok, et vissiin tarvii koodia sitten : ( ")

