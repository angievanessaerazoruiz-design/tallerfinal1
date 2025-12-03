# Contar cuántas veces aparece cada letra en una cadena.


texto = "hola hola"
conteo = {}

for letra in texto:
    if letra != " ":
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1

print(conteo)