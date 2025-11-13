

#Pide una contraseña y verifica si cumple ciertos requisitos (mayúsculas, minúsculas, numeros).

c = input("Contraseña: ")
if any(x.isupper() for x in c) and any(x.islower() for x in c) and any(x.isdigit() for x in c):
    print("Segura ✅")
else:
    print("Insegura ❌")
