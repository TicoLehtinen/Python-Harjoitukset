## 5. Tehtävä

print("anna leiviskien määrä:")
leiviskat = float(input())
print("leiviskien paino on " + str(leiviskat * 8.512) + " kg")
print("anna naulojen määrä:")
naulat = float(input())
print("naulojen paino on " + str(naulat * 0.426) + " kg")
print("anna luotien määrä:")
luodit = float(input())
print("luotien paino on " + str(luodit * 0.0133) + " kg")
print("massa on nykymittojen mukaan " + str(leiviskat * 8.512 + naulat * 0.426 + luodit * 0.0133) + " kg,") 