
#Calcula el promedio de tres notas y determina si el estudiante aprueba o reprueba (minimo 60).


n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

prom = (n1 + n2 + n3) / 3

if prom >= 60:
    print("Aprobado")
else:
    print("Reprobado")