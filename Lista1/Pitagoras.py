#João Rafael

print("Pitágoras descobriu que a soma do quadrado dos catetos de um triângulo retângulo é igual ao quadrado de sua hipotenusa")
print("\nPara calcular a hipotenusa, digite os catetos\n")

cat1 = int(input("Primeiro Cateto = "))
cat2 = int(input("Segundo Cateto = "))

hipot = (cat1 ** 2) + (cat2 ** 2)
hipot = hipot ** 0.5

print("\n\nHipotenusa = ", hipot)
