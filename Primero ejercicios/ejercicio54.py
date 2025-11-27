

#Escribe un programa que reciba una calificación numérica (0 a 100) y determine la
#categoría de la nota: "Muy deficiente" (menos de 50), "Deficiente" (50-64), "Regular"
#(65-74), "Buena" (75-89) y "Excelente" (90-100).


n = int(input("Nota (0-100): "))
if n<50: print("Muy deficiente")
elif n<65: print("Deficiente")
elif n<75: print("Regular")
elif n<90: print("Buena")
else: print("Excelente")