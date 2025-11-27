#crear un algoritmo en python con ciclos for que nos imprima las tablas de multiplicar

numero= int (input("que tabla quieres:"))

for i in range (1, 11):
    print (numero, "x", i, "=", numero * i)