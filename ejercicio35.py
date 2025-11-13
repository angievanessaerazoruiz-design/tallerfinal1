

#Pide un usuario y contraseña y verifica si coinciden con valores predeterminados.

usuario = input("Usuario: ")
clave = input("Contraseña: ")

if usuario == "admin" and clave == "1234":
    print("Acceso permitido")
else:
    print("Acceso denegado")