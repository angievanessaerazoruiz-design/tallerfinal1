
#Pide un número y muestra la raíz cuadrada si es positivo. Si es negativo, muestra un 
#mensaje diciendo que no tiene raíz real.


import math 
n = float(input("Ingrese un número: "))

if n >= 0:
    print("La raíz cuadrada es:", math.sqrt(n))
else:
    print("No tiene raíz real")