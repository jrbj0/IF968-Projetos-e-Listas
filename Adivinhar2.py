print("Bem vindo ao RETORNO DO JOGO DA ADIVINHAÇÃO, Jogador 1")
print("Por favor, digite dois números de 0 a 100 para o Jogador 2 adivinhar")

numero1 = 101
numero2 = 102

while numero1 < 0 or numero1 > 100:
    numero1 = int(input("Seu primeiro número: "))
    
while numero2 == numero1 and numero2 < 0 or numero2 > 100:
    numero2 = int(input("Seu segundo número: "))


print("\n" * 80)

print("Bem vindo ao RETORNO DO JOGO DA ADIVINHAÇÃO, Jogador 2")
print("O Jogador 1 deu 2 números para você adivinhar, você tem 5 chances!\n")



acertou1 = acertou2 = False
tentativa = 0

while(tentativa != 5 and (not acertou1 or not acertou2)):
    
    palpite = int(input("Seu palpite: "))

    if(numero1 == palpite):
        if(acertou1):
            print("\nVocê já acertou o primeiro número...\n\n")
        else:
            print("\n\nVOCÊ CONSEGUIU ADIVINHAR O NÚMERO 1!\n\n")
            acertou1 = True
    if(numero2 == palpite):
        if(acertou2):
            print("\nVocê já acertou o segundo número...\n\n")
        else:
            print("\n\nVOCÊ CONSEGUIU ADIVINHAR O NÚMERO 2!\n\n")
            acertou2 = True
        
    if(numero1 > palpite and numero2 > palpite):
        print("\nAmbos os números são MAIORES que", palpite, "\n\n")
    if(numero1 < palpite and numero2 < palpite):
        print("\nAmbos os números são MENORES que", palpite, "\n\n")

    if((numero1 > palpite and numero2 < palpite)
       or (numero1 < palpite and numero2 > palpite)):
        print("\n" + str(palpite), "está entre os números\n")
        if(palpite == (numero1 + numero2)/2):
            print("...E de alguma forma você conseguiu acertar a média dos dois números!\n")
    
    tentativa = tentativa + 1

    
if(acertou1 and acertou2):
    print("\n\nPARABÉNS, VOCÊ CONSEGUI ACERTAR AMBOS OS NÚMEROS DO JOGADOR 1!")
else:
    print("\n\n\n\nInfelizmente você não conseguiu adivinhar os números do Jogador 1...")
    print("Os número do Jogador 1 eram", numero1, "e", numero2)
    print("Boa sorte na próxima!")


    
