
#Pide peso y altura, calcula el IMC y clasifícalo en "Bajo peso", "Normal", "Sobrepeso" o "Obesidad".


peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")