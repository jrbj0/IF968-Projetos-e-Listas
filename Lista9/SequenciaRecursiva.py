#João Rafael

def sequencia(qtd, num = 0):
    if qtd:
        num = sequencia(qtd - 1, num + ( ((qtd * 2) - 1) / qtd ))
    return num

print("INSIRA 0 PARA ENCERRAR")
print("\n[1] + 3/[2] + 5/[3] + 7/[4] +...")
quantidade = 1
while quantidade > 0:
    quantidade = int(input("\nQuantidade: "))
    print(round(sequencia(quantidade), 4))

        
