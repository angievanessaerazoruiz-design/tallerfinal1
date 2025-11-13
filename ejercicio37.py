

#Pide el monto de una transferencia y el saldo disponible, y detecta si la transacción es fraudulenta.


saldo = float(input("Saldo disponible: "))
monto = float(input("Monto a transferir: "))

if monto > saldo:
    print("Transacción fraudulenta o sin fondos.")
else:
    print("Transferencia exitosa.")