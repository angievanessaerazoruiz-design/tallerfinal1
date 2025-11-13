

#Pide un número entre 1 y 7 y muestra el día correspondiente.

num = int(input("Número (1-7): "))
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

if 1 <= num <= 7:
    print("Día:", dias[num - 1])
else:
    print("Número fuera de rango")