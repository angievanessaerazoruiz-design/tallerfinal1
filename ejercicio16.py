
#Pide una calificación y clasifícala en "Excelente", "Buena", "Regular" o "Mala".

cal= float (input("ingresa tu calificacion:"))

if cal >= 9:
    print("excelente")
elif cal >= 7:
    print("buena")
elif cal >= 5:
    print ("regular")
else:
    print("mala")