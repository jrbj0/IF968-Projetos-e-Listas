#Joao Rafael

numero = int(input("INSIRA O NÚMERO: "))
listanumeros = []

for i in range(1, numero):
    if numero % i == 0:
        listanumeros.append(i)

stringnumeros = ""
somanumeros = 0
for i in range(0, len(listanumeros)):
    somanumeros += listanumeros[i]
    
    if i != 0:
        stringnumeros = stringnumeros + " + "    
    stringnumeros = stringnumeros + str(listanumeros[i])
    
print(numero, " =", stringnumeros)

if somanumeros == numero:
    print(numero, "é um número perfeito!")
else:
    print(numero, "não é um número perfeito!")
