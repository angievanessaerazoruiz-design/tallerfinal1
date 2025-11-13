

#Pide un puntaje de examen y determina en qué rango cae (por ejemplo, A, B, C, D, o F).

p = int(input("Puntaje: "))

if p >= 90:
    print("A")
elif p >= 80:
    print("B")
elif p >= 70:
    print("C")
elif p >= 60:
    print("D")
else:
    print("F")