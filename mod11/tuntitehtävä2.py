try:
    print("Anna luku")
    a = float(input())
    print("Anna toinen luku")
    b = float(input())
    print(a / b)

except ValueError:
    print("Virhe: anna numero, älä merkkejä!")
except ZeroDivisionError:
    print("Virhe: nollalla ei voi jakaa!")