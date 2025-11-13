

#Pide dos números y un operador, y realiza una operación considerando casos especiales de division


a = float(input("Número 1: "))
b = float(input("Número 2: "))
op = input("Operador (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print("Error: división por cero" if b == 0 else a / b)
else:
    print("Operador no válido")