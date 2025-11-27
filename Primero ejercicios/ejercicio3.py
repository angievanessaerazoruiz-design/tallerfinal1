
#Crea un programa que pida la edad de una persona y determine si es un niño (0-12
#años), un adolescente (13-17 años), un adulto (18-64 años) o un adulto mayor (65 años o mas).



edad = int(input("Ingrese su edad: "))

if edad <= 12:
    print("Es un niño (0 a 12 años)")
elif edad <= 17:
    print("Es un adolescente (13 a 17 años)")
elif edad <= 64:
    print("Es un adulto (18 a 64 años)")
else:
    print("Es un adulto mayor (65 años o más)")