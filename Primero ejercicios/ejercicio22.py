
#Pide dos números y muestra cuál está más cerca de 100.

a = float(input("Número 1: "))
b = float(input("Número 2: "))

if abs(100 - a) < abs(100 - b):
    print(a, "está más cerca de 100")
else:
    print(b, "está más cerca de 100")