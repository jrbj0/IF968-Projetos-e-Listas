# -*- coding: utf8 -*-
import sys
from os import rename, remove


############PRINCIPAL############

def processarComandos(comandos) :

    #Checa se o usuário colocou os comandos
    if len(comandos) - 1:
        switchOperacoes = {"A": adicionar,
                           "R": remover,
                           "F": fazer,
                           "P": priorizar,
                           "L": listar}

        #dict.get(key, default)
        #Evita que o dicionário devolva um erro caso a key não esteja nele, como um default
        switchOperacoes.get(comandos[1].upper(), ajuda)(comandos[2:])
        
    #Caso o usuário tenha rodado sem os comandos
    else:
        ajuda()


def ajuda(x = ""):
    print("\n\n\nO template de entrada é:\n" +
          "21102015 0429 OPERAÇÃO Descrição (PRIORIDADE) @Contexto +Projeto \n\n" +
          "Data e Hora são opcionais, mas devem ser colocadas neste formato, sem símbolos\n" +
          "As operações são: [A]dicionar, [R]emover, [F]azer, [P]riorizar e [L]istar\n" +
          "Descrição é todo o texto que não se encaixa nas outras definições\n" +
          "A PRIORIDADE é definida por somente uma letra de A a Z entre parênteses\n" +
          "Contexto indica onde a atividade será realizada e deve possuir um @ antes\n" +
          "Projeto serve para agrupar atividades relacionadas e deve possuir um + antes\n" +
          "\nFeito por André Loponte e João Rafael")
    

def organizar(item):

    extras = {"data": ["", dataValidacao],
              "hora": ["", horaValidacao],
              "prio": ["", prioridadeValidacao],
              "cont": ["", contextoValidacao],
              "proj": ["", projetoValidacao]}

    descricao = ""
    for i in range(len(item)):
        validado = False
        for j in extras:
            if not extras[j][0]:
                extras[j][0] = validar(extras[j][0], item[i], extras[j][1])
                validado = True
        if not validado and not extras["cont"][0] and not extras["proj"][0]:
            descricao += " " + item[i]

            ########################
            # DESCRIÇÃO ESTÁ VAZIA #
            ########################

    extrasFinais = [extras["data"][0], extras["hora"][0],
                    extras["prio"][0], extras["cont"][0],
                    extras["data"][0]]

    print(descricao.strip())

    return (descricao.strip(), [extrasFinais])

def validar(atributo, item, funcao):
    if funcao(item) and not atributo:
        return item
    return atributo

  
############OPERAÇÕES############

def adicionar(descricao):##FAZER

    print(descricao)

    if not descricao:
        return
    
    try: 
        fp = open(TODO_FILE, 'a')
        fp.write(novaAtividade + "\n")
        fp.close()
    except IOError as err:
        print("Não foi possível escrever para o arquivo " + TODO_FILE)
        print(err)
        return False

    return True

def remover(num):##FAZER

    return


def fazer(num):##FAZER

    return


def priorizar(num, prioridade):##FAZER

    return


def listar():##FAZER

    return


############ARQUIVO############

#Pega todas as linhas do arquivo e passa pelo lerItem
def lerArquivo():

    f = open(arquivo_TODO, "a+")
    f.seek(0)
    linhas = f.readlines()
    linhas = limparLista(linhas)

    listas = []
    for i in range(len(linhas)):
        listas.append(linhas[i])
        listas[i] = listas[i].split(" ")
        listas[i] = organizar(listas[i])        

    return listas
  

############ORDENAR############


def ordenarPorDataHora(itens):##FAZER

  ##

  return itens


def ordenarPorPrioridade(itens):##FAZER

  ##

  return itens


############VALIDAÇÃO############

def prioridadeValidacao(pri):

    pri = pri.upper()
    if len(pri) == 3:
        if pri.startswith("(") and pri.endswith(")"):
            if pri[1] >= "A" and pri[1] <= "Z":
                return True  
    return False

def horaValidacao(horaMin):
    
    if len(horaMin) == 4 and soDigitos(horaMin):
        if int(horaMin[0:2]) < 24 and int(horaMin[2:4]) < 60:
            return True        
    return False
    
def dataValidacao(data):

    if len(data) == 8 and soDigitos(data):        
        dia = int(data[0:2])
        mes = int(data[2:4])       
        ano = int(data[4:])
        
        if mes > 0 and mes <= 12:

            #Checa o número de dias de cada mês
            #Eu não encontrei uma lógica melhor
            #Claro, dava pra inserir manualmente os meses
            #Mas não teria graça
            if mes <= 7:
                dias = 30       #2, 4 e 6
                if mes % 2:
                    dias = 31   #1, 3, 5 e 7                    
            elif mes > 7:
                dias = 31       #8, 10, 12
                if mes % 2:
                    dias = 30   #9 e 11
                    
            #Checa se é bissexto, mesmo que não precise
            if mes == 2:
                dias = 28
            if not ano % 4 and (ano % 100 or not ano % 400):            
                dias = 29
                
        #Mês inválido
        else:
            return False
        
        if dia > 0 and dia <= dias:
            return True
        
    return False


def projetoValidacao(proj):
    return projcontValidacao("+", proj)

def contextoValidacao(cont): 
    return projcontValidacao("@", cont)

def projcontValidacao(simbolo, texto):
    if len(texto) > 1 and texto.startswith(simbolo):
        return True
    return False


############UTILIDADES############

def printCores(texto, cor, resetar = True):
    
    switchCores = {"RED":       "\033[1;31m",
                   "BLUE":      "\033[1;34m",
                   "CYAN":      "\033[1;36m",
                   "GREEN":     "\033[0;32m",
                   "YELLOW":    "\033[0;33m",
                   "BOLD":      "\033[;1m",
                   "REVERSE":   "\033[;7m",
                   "RESET":     "\033[0;0m"}
    reset = ""
    if resetar:
        reset = switchCores["RESET"]

    print(switchCores.get(cor, "") + texto + reset)


def soDigitos(numero):
    
    if type(numero) != str :
        return False
    for x in numero :
        if x < "0" or x > "9" :
            return False
    return True


def strItem(item):
    texto = item[0] + " "
    extras = item[1]
    
    for i in extras:
        if i:
            texto += i + " "
    return texto.strip()


def limparTela():
    
    print("\n"*50)


def limparLista(lista):

    listaFinal = []
    while lista:
        item = lista.pop(0).strip()
        if item:
            listaFinal.append(item)
    return listaFinal


############EXECUÇÃO############

arquivo_TODO = "todo.txt"
arquivo_DONE = "done.txt"

organizar("11092005 0911 (A) descricao descricao 1102 @contexto 1102 descartar +projeto +projeto2".split(" "))

processarComandos(sys.argv)

#while printCores(strItem(organizar(input("ORGANIZAR: ").split(" "))), "RED"):
 #   pass
