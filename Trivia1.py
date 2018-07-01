import time
from random import randint

listaPerguntas = ["AAA\n\n1)A\n2)B\n3)C\n4)D\n5)E",
                  "BBB\n\n1)A\n2)B\n3)C\n4)D\n5)E",
                  "CCC\n\n1)A\n2)B\n3)C\n4)D\n5)E",
                  "DDD\n\n1)A\n2)B\n3)C\n4)D\n5)E",
                  "EEE\n\n1)A\n2)B\n3)C\n4)D\n5)E",
                  "FFF\n\n1)A\n2)B\n3)C\n4)D\n5)E",
                  "GGG\n\n1)A\n2)B\n3)C\n4)D\n5)E",
                  "HHH\n\n1)A\n2)B\n3)C\n4)D\n5)E",
                  "III\n\n1)A\n2)B\n3)C\n4)D\n5)E",
                  "JJJ\n\n1)A\n2)B\n3)C\n4)D\n5)E"]

listaRespostas = ["1", #1
                  "2", #2
                  "3", #3
                  "4", #4
                  "5", #5
                  "1", #6
                  "2", #7
                  "3", #8
                  "4", #9
                  "5"] #10

resultadoCorreto = ["Boa, cara!",
                    "Não esperava que você fosse acertar essa!",
                    "Olha lá, seu QI ainda está positivo!",
                    "Essa foi fácil demais...",
                    "Ok, até meu cachorro acertaria essa!",
                    "Muito massa, velho!"]

resultadoIncorreto = ["VAI ESTUDAR, SEU SEM CULTURA!",
                      "MINHA VÓ ACERTARIA ISSO\nE ELA TÁ EM COMA!!!",
                      "VOCÊ TA PELO MENOS TENTANDO?",
                      "COMO ASSIM VOCÊ NÃO SABIA DISSO?",
                      "SEU ACATALÉPTICO!",
                      "VOCÊ E SÓ UM VANÍLOQUO",
                      "CÉREBRO DE ANELÍDIO!",
                      "FORA TEMER"]
                      

print("BEM VINDO AO QUIZ TRIVIA DA CRUELDADE!\n"
      "Quantas perguntas você deseja responder? (0 - 5)")

OK = False
while OK == False:
    try:
        numeroPerguntas = int(input())
        print()
        if numeroPerguntas >= 0 and numeroPerguntas <= 10:
            numeroPerguntas = numeroPerguntas * 2
            if numeroPerguntas == 0:
                numeroPerguntas = 10
            OK = True
            
    except ValueError:
        print()

print("Ok, vão ser", numeroPerguntas, "questões, se prepare!\n\n")

pontos = 0
numPerguntaAtual = 0
numPerguntaJogador = 0

while numeroPerguntas != 0:
    numPerguntaJogador = numPerguntaJogador + 1
    numPerguntaAtual = randint(0, len(listaPerguntas)-1)
    print("\n\n" + str(numPerguntaJogador) + "ª Pergunta:\n")
    print(listaPerguntas[numPerguntaAtual])
    palpite = input("\nResposta: ")
    if (palpite.lower == listaRespostas[numPerguntaAtual].lower):
        pontos = pontos + 1
        print(resultadoCorreto[randint(0, len(resultadoCorreto) -1)])
    else:
        print(resultadoIncorreto[randint(0, len(resultadoIncorreto) -1)])
    listaPerguntas.pop(numPerguntaAtual)
    listaRespostas.pop(numPerguntaAtual)
    numeroPerguntas = numeroPerguntas - 1


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("SEU RESULTADO FOI...")
time.sleep(5)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("SEU RESULTADO FOI...", pontos, "de", numPerguntaJogador, "perguntas!")

resultado = pontos / numPerguntaJogador

if resultado == 1:
    print("CARAMBA, ALGUÉM COM UM CÉREBRO FUNCIONAL!!!\nMEUS PARABÉNS, AMIGO, VOCÊ MERECE!")
    parar = True
    
if resultado > 0.5  and !parar:    
    print("OH, SÓ FALTAM ALGUNS PONTOS DE QI PRA VOCÊ")
    break;
          
    

