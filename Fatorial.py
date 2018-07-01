def fatorial(x):
    resultado = 1
    for i in range(2, x + 1):
        resultado = resultado * i
    return resultado

numero = 1

while(numero != 0):
    numero = int(input("NUMERO: "))
    fator = fatorial(numero)
    print(fator)
