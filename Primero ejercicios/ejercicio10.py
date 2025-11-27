
#Pide la edad y determina el descuento: 50% si es menor de 12, 20% si es mayor de 65, y 
#sin descuento para los demás.



edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Descuento del 50%")
elif edad > 65:
    print("Descuento del 20%")
else:
    print("Sin descuento")