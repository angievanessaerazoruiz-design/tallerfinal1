

#Pide un tipo de sangre y determina a qué grupos puede donar y recibir.



t = input("Tipo (A, B, AB, O): ").upper()
if t=="A": print("Dona A,AB / Recibe A,O")
elif t=="B": print("Dona B,AB / Recibe B,O")
elif t=="AB": print("Dona AB / Recibe todos")
elif t=="O": print("Dona todos / Recibe O")
else: print("Inválido")