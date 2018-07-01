Perguntas = ["Quem são os pais de Thor?",
             "Quem é a mãe de Sleipnir?",
             "Como são chamadas as mulheres que revelaram o início e o fim do mundo para Odin?",
             "Qual o nome das correntes que prendem Fenrir?",
             "Quem é chamado de 'o Pai de Todos'"]
             
Respostas = ["Odin e Jord",
             "Loki",
             "Volur",
             "Gleipnir",
             "Odin"]

Xingamentos = ["JÁ COMEÇOU ERRANDO!?",
              "VOCÊ ESTÁ PELO MENOS TENTANDO?",
              "MAS É MUITO BURRO MESMO!",
              "QUE DEMÊNCIA!",
              "SEU QI É NEGATIVO!"]

print("play(showdomilhao.mp3)" , "\n" * 42)
print("Bem vindo ao Trivia da Mitologia Nórdica!\n")


perguntasRestantes = 5
perguntaAtual = 0

pontos = 0


while perguntasRestantes != 0:

    print("\n\n")
    print(str(perguntaAtual + 1) + "ª Pergunta:\n")    
    print(Perguntas[perguntaAtual])
    
    palpite = input("\nResposta: ")    
    if (palpite.lower() == Respostas[perguntaAtual].lower()):
        pontos = pontos + 1
        print("Acertou!")        
    else:
        print(Xingamentos[perguntaAtual])

    perguntasRestantes = perguntasRestantes - 1
    perguntaAtual = perguntaAtual + 1



print("\n\n\nVocê conseguiu", pontos, "pontos...\n")

      
if pontos == 5:
    print("MEUS PARABÉNS!\nALÉM DE TER UM CÉREBRO FUNCIONAL VOCÊ CONHECE A MITOLOGIA NÓRDICA!")

elif pontos > 0 and pontos < 5:
    print("VAI ESTUDAR MITOLOGIA NÓRDICA, SEU SEM CULTURA!")

else:
    print("QUEM DIRIA QUE VOCÊ IRIA CONSEGUIR MAIS PONTOS QUE SEU QI!")


