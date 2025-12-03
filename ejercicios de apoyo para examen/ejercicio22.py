
# Encontrar el número más grande en una lista de números. (numeros = [3, 15, 8, 23, 42, 16])

numeros = [3, 15, 8, 23, 42, 16]
mayor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n

print(mayor)