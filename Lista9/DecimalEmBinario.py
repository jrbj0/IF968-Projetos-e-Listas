#João Rafael

def binario(num, resultado = ""):
    if num and num <= 1000000000:
        resultado = binario(int(num/2), str(num % 2) + resultado)
    return resultado

print("INSIRA 0 PARA ENCERRAR")
numero = 1
while numero > 0:
    numero = int(input("\nNúmero: "))
    if numero:
        print(binario(numero))
