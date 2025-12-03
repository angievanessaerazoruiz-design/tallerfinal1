
# Calcular la suma de los dígitos de un número (ejemplo, 12345).

num = 12345
suma = 0

for d in str(num):
    suma += int(d)

print(suma)