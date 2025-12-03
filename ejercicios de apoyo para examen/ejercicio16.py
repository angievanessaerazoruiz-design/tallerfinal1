
# Contar cuántos números del 1 al 100 son divisibles por 3.

cont = 0

for i in range(1, 101):
    if i % 3 == 0:
        cont += 1

print(cont)