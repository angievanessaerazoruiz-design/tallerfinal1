
#Pide tres números y muestra si son todos pares, todos impares, o hay mezcla.

a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))

if a%2==0 and b%2==0 and c%2==0:
    print("Todos son pares")
elif a%2!=0 and b%2!=0 and c%2!=0:
    print("Todos son impares")
else:
    print("Hay mezcla de pares e impares")