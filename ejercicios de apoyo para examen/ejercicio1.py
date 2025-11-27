#utilizando funciones y ciclo for determinar si una lista esta ordenada

def listaordenada (lista):
    for i in range (len(lista)-1):
        if lista [i] > lista [i+1]:
            return False
    return True

milista = [1,2,3,5,6,7,8,9]

if listaordenada (milista):
    print ("la lista esta ordenada.")
else:
    print ("la lista no esta ordenada.")
