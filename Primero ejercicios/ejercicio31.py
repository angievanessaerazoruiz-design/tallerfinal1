

#Pide la edad y determina si la persona puede votar, y si es obligatorio (entre 18 y 70 años).


edad = int(input("Edad: "))

if edad < 18:
    print("No puede votar")
elif edad <= 70:
    print("Voto obligatorio")
else:
    print("Voto opcional")