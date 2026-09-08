vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät",
              "kesä", "kesä", "kesä", "syksy", "syksy",
              "syksy", "talvi")
print("Anna kuukauden numero (1-12): ") 
kuukausi = int(input())

if 1 <= kuukausi <= 12:
    print("Vuodenaika on:", vuodenajat[kuukausi - 1])
else:
    print("Virheellinen kuukauden numero.")