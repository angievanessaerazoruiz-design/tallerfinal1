

#Pide dos números y determina si son pares o impares y si uno es múltiplo del otro.a,b = int(input()), int(input())


a,b = int(input()), int(input())
print("a par" if a%2==0 else "a impar")
print("b par" if b%2==0 else "b impar")
print("Múltiplos" if a%b==0 or b%a==0 else "No múltiplos")