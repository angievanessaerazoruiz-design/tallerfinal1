
#Pide un mes (número) e indica a qué trimestre del año pertenece.

mes = int(input("Ingresa el número del mes (1-12): "))

if mes <= 3:
    print("Primer trimestre")
elif mes <= 6:
    print("Segundo trimestre")
elif mes <= 9:
    print("Tercer trimestre")
else:
    print("Cuarto trimestre")