# Parcial semestre pasado: sobre el coll senter

print("-----------------------------")
print("---Descuentos-coll-senter----")
print("-----------------------------")

a=input("Dame el nombre del producto #1: " )
a1=float(input("ingrese el valor del producto #1: " ))
b=input("Dame el nombre del producto #2: " )
b1=float(input("ingrese el valor del producto #2: " ))
c=input("Dame el nombre del producto #3: " )
c1=float(input("ingrese el valor del producto#3: " ))

# proceso
if  0 <= a1 <= 9999999 and 0 <= b1 <=9999999 and 0 <= c1 <=9999999:
    if c1<b1<a1:
         A = c1+b1
    elif a1<c1<b1:
         A = a1+c1
    elif b1<a1<c1:
         A = b1+a1
else:
    print("Algo susedio, no es valido lo que ingresaste")


print("--------------------------------------------------")
print("---Gracias por comprar en el mejor supermerado---")
print("Tu descuento por el dia de la madre es: " + str(A))
