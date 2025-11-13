
#Pide una velocidad y clasifícala en "Baja", "Normal" o "Alta".


v = float(input("Ingresa la velocidad: "))

if v < 40:
    print("Baja")
elif v <= 80:
    print("Normal")
else:
    print("Alta")