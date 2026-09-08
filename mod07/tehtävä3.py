def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

print("Anna gallonamäärä (negatiivinen lopettaa):")
gallonat = float(input())

while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print("Litroina:", litrat)
    print("Anna gallonamäärä (negatiivinen lopettaa):")
    gallonat = float(input())