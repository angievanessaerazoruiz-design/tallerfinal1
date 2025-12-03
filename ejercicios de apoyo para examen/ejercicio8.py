# Eliminar duplicados de una lista. (lista = [1, 2, 2, 3, 4, 4, 5])

lista = [1, 2, 2, 3, 4, 4, 5]

sin_duplicados = []

for numero in lista:
    if numero not in sin_duplicados:
        sin_duplicados.append(numero)

print(sin_duplicados)