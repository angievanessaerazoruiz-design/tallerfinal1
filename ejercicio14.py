
#Pide el total de la compra e indica si tiene 10% de descuento si es mayor a 100.


total = float(input("Ingrese el total de la compra: "))

if total > 100:
    total *= 0.9  # aplica 10% de descuento
    print("Tiene 10% de descuento. Total a pagar:", total)
else:
    print("Sin descuento. Total a pagar:", total)