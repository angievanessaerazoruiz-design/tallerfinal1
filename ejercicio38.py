

#Pide una temperatura y clasifícala como "Muy frío", "Frío", "Tibio", "Caliente", o "Muy caliente".

temp = float(input("Temperatura: "))

if temp < 5:
    print("Muy frío")
elif temp < 15:
    print("Frío")
elif temp < 25:
    print("Tibio")
elif temp < 35:
    print("Caliente")
else:
    print("Muy caliente")