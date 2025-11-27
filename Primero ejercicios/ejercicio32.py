

#Pide una temperatura en grados Celsius y convierte a Fahrenheit o Kelvin.

c = float(input("Temperatura en °C: "))
op = input("Convertir a (F/K): ").upper()

if op == "F":
    print("Fahrenheit:", c * 9/5 + 32)
elif op == "K":
    print("Kelvin:", c + 273.15)
else:
    print("Opción no válida")