
#Pide el número de horas trabajadas y calcula el salario con 50% más para horas extra.

horas = float(input("Horas trabajadas: "))
salario = horas * 10 if horas <= 40 else (40 * 10) + ((horas - 40) * 10 * 1.5)
print("Salario total:", salario)