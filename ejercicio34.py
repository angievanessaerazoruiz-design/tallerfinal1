

#Pide la categoría del cliente y calcula el descuento en base a la categoría.

cat = input("Categoría (A, B, C): ").upper()

if cat == "A":
    desc = 0.20
elif cat == "B":
    desc = 0.10
else:
    desc = 0.05

print("Descuento:", desc * 100, "%")