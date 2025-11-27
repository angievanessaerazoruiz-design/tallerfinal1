

#Pide una temperatura y verifica si está en rango de ebullición o congelación.


temp = float(input("Temperatura en °C: "))

if temp <= 0:
    print("Congelación")
elif temp >= 100:
    print("Ebullición")
else:
    print("Temperatura normal")
    