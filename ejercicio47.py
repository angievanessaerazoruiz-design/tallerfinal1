

#Pide el precio de un producto y si es esencial o no, y aplica IVA según el tipo.


p = float(input("Precio: "))
e = input("¿Es esencial? (s/n): ")
print("Total:", p*1.05 if e=="s" else p*1.19)
