print("Bem vindo ao jogo da advinhação, Jogador 1")
print("Por favor, digite um número de 0 a 100 para o Jogador 2 adivinhar")

numero1 = 101
palpite = 101
tentativa = 0

while numero1 < 0 or numero1 > 100:
    numero1 = int(input("Seu número: "))

print("\n" * 80)
print("Bem vindo ao jogo da advinhação, Jogador 2")
print("O Jogador 1 deu um número para você adivinhar, você tem 3 chances!\n")



while(tentativa != 3):
    
    palpite = int(input("Sua resposta: "))

    if(numero1 == palpite):
        print("\n\nPARABÉNS, VOCÊ CONSEGUIU ADIVINHAR O NÚMERO DO JOGADOR 1!")
        break
    elif(numero1 > palpite):
        print("\nO número é MAIOR que", palpite, "\n\n")
    elif(numero1 < palpite):
        print("\nO número é MENOR que", palpite, "\n\n")
    
    tentativa = tentativa + 1
    

else:
    print("\n\n\n\nInfelizmente você não conseguiu adivinhar o número do Jogador 1...")
    print("O número do Jogador 1 era", numero1)
    print("Boa sorte na próxima!")


    
