

#Pide cinco calificaciones y calcula el promedio, luego muestra el nivel de desempeño
#(bajo, medio, alto).

notas = [float(input(f"Nota {i+1}: ")) for i in range(5)]
prom = sum(notas) / 5

if prom < 3:
    print("Desempeño bajo")
elif prom < 4:
    print("Desempeño medio")
else:
    print("Desempeño alto")
