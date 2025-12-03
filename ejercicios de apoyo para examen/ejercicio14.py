 # Calcular el factorial de un número dado (por ejemplo, 5).
 

n = 5
fact = 1

for i in range(1, n+1):
    fact *= i

print(fact)