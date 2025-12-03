# Imprimir la primera y última letra de cada palabra en una frase. frase =  "Este es ejemplo"

frase="este es un ejemplo"
palabras = frase.split()

for p in palabras:
    print(p[0], p[-1])

