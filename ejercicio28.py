
#Pide un mes y determina si está dentro del ciclo escolar o en vacaciones.

mes = int(input("Mes (1-12): "))

if 1 <= mes <= 6 or 8 <= mes <= 11:
    print("Ciclo escolar")
else:
    print("Vacaciones")