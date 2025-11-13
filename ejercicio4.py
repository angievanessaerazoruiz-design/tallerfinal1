#Escribe un programa que le pida al usuario su calificación y determine si aprobó (60 o
#más), reprobó (menos de 60), y si es un aprobado especial (90 o más).

nota = float(input("Ingrese su calificación: "))

if nota >= 90:
    print("Aprobado con mención especial")
elif nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")