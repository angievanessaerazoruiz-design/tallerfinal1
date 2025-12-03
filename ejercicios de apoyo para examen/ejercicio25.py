
# Contar cuántos números en una lista son mayores que un valor dado (ej. 10). numeros = [5, 12, 3,
#18, 25, 7]


numeros = [5, 12, 3, 18, 25, 7]
valor = 10
cont = 0

for n in numeros:
    if n > valor:
        cont += 1

print(cont)