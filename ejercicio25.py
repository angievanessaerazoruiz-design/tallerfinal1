
#Pide una letra y determina si es vocal o consonante.

letra = input("Ingresa una letra: ").lower()

if letra in "aeiou":
    print("Es vocal")
else:
    print("Es consonante")