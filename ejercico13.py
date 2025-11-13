
#Pide dos letras e indica si son iguales o cuál es mayor alfabéticamente.


l1 = input("Ingrese la primera letra: ")
l2 = input("Ingrese la segunda letra: ")

if l1 == l2:
    print("Son iguales")
elif l1 < l2:
    print(l1, "es menor alfabéticamente que", l2)
else:
    print(l1, "es mayor alfabéticamente que", l2)