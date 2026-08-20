print("Minkä hytin haluaisit valita? Vaihtoehdot ovat LUX, A, B ja C.")
hytti = input() 

if hytti == "LUX" or hytti== "lux": print("LUX hytti on parvekkeellinen hytti, joka sijaitsee yläkannella.")
elif hytti == "A" or hytti == "a": 
 print("A hytti on ikkunallinen hytti, joka sijaitsee autokannen yläpuolella.") 
elif hytti == "B" or hytti =="b": 
 print("B hytti on ikkunaton hytti, joka sijaitsee autokannen yläpuolella.")
elif hytti == "C" or "c": print("C hytti on ikkunaton hytti, joka sijaitsee autokannen alapuolella.")   
else: 
 print("Virheellinen hyttiluokka. valitse jokin toinen vaihtoehto.")

