

#Pide un día de la semana y determina si es fin de semana o día laboral.


d = input("Día: ").lower()
print("Fin de semana" if d in ["sabado","sábado","domingo"] else "Laboral")