

#Escribe un programa que pida un número de mes (1 para enero, 2 para febrero, etc.) y
#determine en qué trimestre del año se encuentra.

m = int(input("Mes (1-12): "))
if m<=3: print("1° trimestre")
elif m<=6: print("2° trimestre")
elif m<=9: print("3° trimestre")
elif m<=12: print("4° trimestre")
else: print("Inválido")