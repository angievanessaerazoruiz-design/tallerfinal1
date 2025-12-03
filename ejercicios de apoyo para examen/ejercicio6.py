# Encontrar el segundo número más grande en una lista de números. (10,15, 20, 25, 5)

numeros = [10, 15, 20, 25, 5]

mayor = numeros[0]
segundo_mayor = numeros[0]

for n in numeros:
    if n > mayor:
        segundo_mayor = mayor
        mayor = n
    elif n > segundo_mayor and n != mayor:
        segundo_mayor = n

print("El segundo número más grande es:", segundo_mayor)