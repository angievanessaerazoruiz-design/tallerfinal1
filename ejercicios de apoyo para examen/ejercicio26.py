
## Encontrar los valores comunes entre dos listas.
#lista1 = [1, 2, 3, 4, 5]
#lista2 = [4, 5, 6, 7, 8]


lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
comunes = []

for x in lista1:
    if x in lista2:
        comunes.append(x)

print(comunes)