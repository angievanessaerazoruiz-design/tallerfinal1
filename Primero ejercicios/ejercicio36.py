

#Pide un código de descuento y aplica un descuento específico si es válido.codigo = input("Ingresa el código de descuento: ")


codigo = input("Ingresa el código de descuento: ")
precio = float(input("Ingresa el precio: "))

if codigo == "DESCUENTO10":
    total = precio * 0.9
    print("Descuento aplicado. Total:", total)
else:
    print("Código inválido. Total:", precio)
    
    
    