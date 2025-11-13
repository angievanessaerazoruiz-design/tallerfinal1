#Escribe un programa que le pida al usuario dos números y un operador (+, -, *, /) y
#realice la operación correspondiente.


a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
op = input("Ingrese el operador (+, -, *, /): ")

if op == "+":
    print("Resultado:", a + b)
elif op == "-":
    print("Resultado:", a - b)
elif op == "*":
    print("Resultado:", a * b)
elif op == "/":
    print("Resultado:", a / b)
else:
    print("Operador no válido")