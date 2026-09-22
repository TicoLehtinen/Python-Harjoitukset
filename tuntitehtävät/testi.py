def lisää_reppuun():
    print("tavara lisättiin reppuun")


print("Haluatko lisätä tavaraa reppuun? (kyllä/ei)")

tavaran_lisäys = input()

while tavaran_lisäys == "kyllä":
    lisää_reppuun()
    break
