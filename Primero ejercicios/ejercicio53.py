

#Una empresa de alquiler de autos permite alquilar vehículos solo a personas mayores de
#21 años. Sin embargo, si la persona tiene entre 21 y 25 años, se le cobra un cargo
#adicional del 15%. Si es mayor de 25, no se cobra ningún cargo adicional. Escribe un
#programa que determine si alguien puede alquilar un auto y el costo adicional si aplica.



e = int(input("Edad: "))
if e<21: print("No puede alquilar")
elif e<=25: print("Cargo 15%")
else: print("Sin cargo")