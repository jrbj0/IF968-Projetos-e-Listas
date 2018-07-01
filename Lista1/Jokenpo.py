#João Rafael

print("Bem-vindo ao Jokenpo, Jogador 1!\n")
print("Digite 'pedra', 'papel' ou 'tesoura' para continuar\n\n")

while(True):
    jogador1 = (input("\nSua jogada: ").lower())

    if(jogador1 == "pedra" or jogador1 == "papel" or jogador1 == "tesoura"):
        break

print("\n" * 100)

#------------------------------------

print("Bem-vindo ao Jokenpo, Jogador 2!\n")
print("Digite 'pedra', 'papel' ou 'tesoura' para continuar\n\n")

while(True):
    jogador2 = (input("\nSua jogada: ").lower())

    if(jogador2 == "pedra" or jogador2 == "papel" or jogador2 == "tesoura"):
        break

print("\n" * 100)

#------------------------------------

print("Jogador 1:", jogador1)
print("Jogador 2:", jogador2, "\n\n")

if(jogador1 == jogador2):
    print("EMPATE!")
    
elif((jogador1 == "pedra" or jogador2 == "pedra") and (jogador2 == "tesoura" or jogador1 == "tesoura")):
    print("Pedra venceu!")

elif((jogador1 == "tesoura" or jogador2 == "tesoura") and (jogador2 == "papel" or jogador1 == "papel")):
    print("Tesoura venceu!")

elif((jogador1 == "papel" or jogador2 == "papel") and (jogador2 == "pedra" or jogador1 == "pedra")):
    print("Papel venceu!")

