 # Convertir una lista de números en una lista de sus cuadrados.
 
numeros = [2, 4, 6, 8]
cuadrados = []  

for n in numeros:
    cuadrado = n * n  
    cuadrados.append(cuadrado)  
print("Lista original:", numeros)
print("Lista de cuadrados:", cuadrados)