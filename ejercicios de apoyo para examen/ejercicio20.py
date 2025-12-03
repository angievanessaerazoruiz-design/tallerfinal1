
# Invertir una cadena usando un ciclo for.


texto = "hola"
invertida = ""

for i in range(len(texto)-1, -1, -1):
    invertida += texto[i]

print(invertida)