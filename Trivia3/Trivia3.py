#João Rafael

from random import randint

def lerArquivo(arquivo):
    
    file = open(arquivo)
    f = file.readlines()
    file.close()
        
    i = 0
    listas = []
    titulo = ""
    perguntas = []
    respostas = []
    while i < len(f) - 1:
        f[i] = f[i].strip()
        if f[i].startswith("TITULO = "):
            titulo = f[i].replace("TITULO = ", "")
        elif f[i] == "***":
            listas.append((titulo, perguntas, respostas))
            titulo = ""
            perguntas = []
            respostas = []
        elif f[i] != "":
            perguntas.append(f[i])
            respostas.append(f[i + 1])
            i += 2        
        i += 1
        
    return listas

def lerXingamentos(arquivo):

    file = open(arquivo)
    f = file.readlines()
    file.close()
    
    xingamentos = []
    for i in range(len(f)):
        xingamentos.append(f[i].strip())

    return xingamentos

def pergunta(perguntaAtual, pontuacao):
    
    print("\n\n")
    print(str(perguntaAtual + 1) + "ª Pergunta:\n")    
    print(Perguntas[perguntaAtual])
    
    palpite = input("\nResposta: ")    
    if (palpite.lower() == Respostas[perguntaAtual].lower()):
        pontuacao = pontuacao + 1
        print("Acertou!")        
    else:
        print(Xingamentos[randint(0, len(Xingamentos) - 1)])

    return pontuacao


def finalizar(pontuacao):    
    print("\n\n\nVocê conseguiu", pontos, "pontos...\n")
      
    if pontuacao == len(Perguntas):
        print("MEUS PARABÉNS!\nVOCÊ TEM UM CÉREBRO FUNCIONAL!")
    elif pontuacao > 0 and pontuacao < len(Perguntas):
        print("VAI ESTUDAR, SEU SEM CULTURA!")
    else:
        print("QUEM DIRIA QUE VOCÊ IRIA CONSEGUIR MAIS PONTOS QUE SEU QI!")

##############       


Listas = lerArquivo("Trivias.txt")
Xingamentos = lerXingamentos("Xingamentos.txt")
print("BEM VINDO À BIBLIOTECA DE TRIVIAS!\n")

for i in range(len(Listas)):
    print(str(i + 1) + ".", Listas[i][0])
    
escolha = -1
while escolha not in range(1, len(Listas) + 1):
    escolha = int(input("\nQUAL TRIVIA VOCÊ DESEJA JOGAR?\n"))
escolha -= 1

print("OK, BOA SORTE!")
titulo = Listas[escolha][0]
Perguntas = Listas[escolha][1]
Respostas = Listas[escolha][2]
input()

print("play(showdomilhao.mp3)" , "\n" * 42)
print("Bem vindo ao Trivia de", titulo + "!")

perguntasRestantes = 5
perguntaAtual = 0
pontos = 0
while perguntasRestantes != 0:

    pontos = pergunta(perguntaAtual, pontos)    
    perguntasRestantes = perguntasRestantes - 1
    perguntaAtual = perguntaAtual + 1

finalizar(pontos)
