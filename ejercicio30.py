
#Pide el ingreso anual y calcula el impuesto basado en tramos de ingresos.

ing = float(input("Ingreso anual: "))

if ing <= 10000:
    imp = ing * 0.05
elif ing <= 30000:
    imp = ing * 0.10
else:
    imp = ing * 0.15

print("Impuesto:", imp)