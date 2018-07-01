#João Rafael

print("Uma equação do segundo grau é formada por 3 números e 1 variável")
print("Ax² + Bx + C\n")
print("Para calcular as raízes, digite 3 valores\n")

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

delta = (B * B) - (4 * A * C)
print("\n\nDelta =", delta)

x1 = (-B + (delta ** 0.5)) / (2 * A)
x2 = (-B - (delta ** 0.5)) / (2 * A)
    
if(delta < 0):
    print("\nNão existem raízes reais pois o Delta é negativo!")
elif(delta == 0):
    print("\nSó existe uma raiz, já que o Delta é 0\n\nX =", x1)
else:
    print("\nX1 =", x1, "\nX2 =", x2)

