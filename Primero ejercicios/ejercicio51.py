

#Un supermercado ofrece descuentos en función de la hora de compra. Si la compra es
# de las 12:00 p.m., se aplica un 10% de descuento. Si la compra es después de las
#6:00 p.m., el descuento es del 20%. En otros horarios, no hay descuento. Escribe un
#programa que determine el descuento aplicable y el total a pagar.


h = int(input("Hora (0-23): "))
p = float(input("Precio: "))
print("Total:", p*0.9 if h<12 else p*0.8 if h>=18 else p)
