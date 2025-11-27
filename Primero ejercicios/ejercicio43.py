

#Pide las edades de tres personas y determina quién es el mayor y quién el menor.


edades = [int(input(f"Edad {i+1}: ")) for i in range(3)]
print("Mayor:", max(edades))
print("Menor:", min(edades))