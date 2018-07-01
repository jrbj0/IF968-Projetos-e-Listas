# -*- coding: utf8 -*-
import sys
from os import rename, remove


########################PRINCIPAL########################

def processarComandos(comandos) :

    #Checa se o usuário colocou os comandos
    if len(comandos) - 1:
        switchOperacoes = {"A": adicionar,
                           "A+": adicionarDesorganizado,
                           "R": remover,
                           "F": fazer,
                           "P": priorizar,
                           "L": listar}

        #Evita que o dicionário devolva um erro caso a key não esteja nele, como um default
        switchOperacoes.get(comandos[1].upper(), ajuda)(comandos[2:])
        
    #Caso o usuário tenha rodado sem os comandos
    else:
        ajuda()


def ajuda(ignorar = ""):
    print("As operações são: [A]dicionar, [R]emover, [F]azer, [P]riorizar e [L]istar\n" +
          "É necessário seguir a ordem, porém, é possível usar [A+] para ignorá-la\n\n" +
          "Exemplo de ordem padrão para adicionar uma atividade:\n" +
          "A 21102015 0429 (PRIORIDADE) Descrição @Contexto +Projeto \n\n" +
          "Data e Hora são opcionais, mas devem ser colocadas neste formato, sem símbolos\n" +   
          "A PRIORIDADE é definida por somente uma letra de A a Z entre parênteses\n" +       
          "Descrição é como será chamada a atividade, não há limitações nesse campo\n" +
          "Contexto indica onde a atividade será realizada e deve possuir um @ antes\n" +
          "Projeto serve para agrupar atividades relacionadas e deve possuir um + antes\n" +
          "\nFeito por André Loponte e João Rafael")
    

def organizar(item, ordem = True):

    extras = {"data": ["", dataValidacao],
              "hora": ["", horaValidacao],
              "prio": ["", prioridadeValidacao],
              "cont": ["", contextoValidacao],
              "proj": ["", projetoValidacao]}

    descricao = ""
    for i in range(len(item)):
        validado = False        
        for j in extras:
            if not validado:                
                #Primeira parte checa se a Data é o primeiro item
                if (not j == "data" or not i) or not ordem:                    
                    #Segunda parte checa se a Hora está antes da descrição e prioridade
                    if not j == "hora" or (not descricao.strip() and not extras["prio"][0]) or not ordem:                        
                        #Terceira parte checa se a prioridade está antes da descrição
                        if not j == "prio" or not descricao.strip() or not ordem:
                           
                            #extras[j][0], validado = validar(extras[j][0], item[i], extras[j][1])
                            extras[j][0], item[i], validado = validar(extras[j][0], item[i], extras[j][1])
                            
                    
        #Finalmente, checa se o item não está vazio e foi encaixado em nenhum dos atributos...
        #E também se já foram colocados o contexto e o projeto
        if not validado and item[i] and ((not extras["cont"][0] and not extras["proj"][0]) or not ordem):
            descricao += " " + item[i]

    extrasFinais = [extras["data"][0],
                    extras["hora"][0],
                    extras["prio"][0],
                    extras["cont"][0],
                    extras["proj"][0]]

    return (descricao.strip(), extrasFinais)


#Função que facilita a organização
#Roda a validação e checa se o atributo já esta preenchido
def validar(atributo, item, funcao):
    if funcao(item):
    #if funcao(item) and not atributo:
        #return item, True
        return item, atributo, True
    #return atributo, False
    return atributo, item, False

  
########################OPERAÇÕES########################

def adicionar(comandos):##FAZER

    
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

def adicionarDesorganizado(descricao):

    return

def remover(num):##FAZER

    return


def fazer(num):##FAZER

    return


def priorizar(num, prioridade):##FAZER

    return


def listar(x):##FAZER

    return



########################ARQUIVO########################

#Pega todas as linhas do arquivo e passa pelo lerItem
def lerArquivo():

    f = open(arquivo_TODO, "a+")
    f.seek(0)
    linhas = f.readlines()
    linhas = limparLista(linhas)

    listas = []
    for i in range(len(linhas)):
        if linhas[i]:
            listas.append(linhas[i])
            listas[i] = listas[i].split(" ")
            listas[i] = organizar(listas[i])

    return listas
  

########################ORDENAR########################

def ordenar(itens):

    #Prioridade
    dictPrio = ordenarPrioridade(itens)
    for i in dictPrio:
        #Data e Hora
        dictPrio[i] = ordenarDataHora(dictPrio[i])
    #Transforma em lista
    itens = dictLista(dictPrio)
    
    return itens


def ordenarDataHora(itens):

    #Junta a data com a hora e organiza de forma crescente
    for i in range(len(itens)):
        for j in range(len(itens) - (1 + i)):            
            iDataHora = rawDataHora(itens[j][0], itens[j][1])
            jDataHora = rawDataHora(itens[j+1][0], itens[j+1][1])
            if iDataHora > jDataHora:
                itens[j], itens[j+1] = itens[j+1], itens[j]
    return itens


def ordenarPrioridade(itens):

    #Organiza as prioridades na ordem alfabética
    for i in range(len(itens)):
        for j in range(len(itens) - (1 + i)):
            if rawPrio(itens[j][2]) < rawPrio(itens[j+1][2]):
                itens[j], itens[j+1] = itens[j+1], itens[j]
    
    #Cria um dicionário com as prioridades usadas    
    dictPrio = {}
    for i in range(len(itens)):
        prio = rawPrio(itens[i][2])
        if not dictPrio.get(prio, ""):
            dictPrio[prio] = []

    #Agrupa listas dentro das prioridades
    for i in dictPrio:
        for j in range(len(itens)):
            if rawPrio(itens[j][2]) == i:
                dictPrio[i].append(itens[j])
                
    return dictPrio


def dictLista(dicionario):

    #Pega todos as keys de um dicionário e as coloca em uma lista
    keys = []
    for i in dicionario:
        keys.append(i)        

    #Organiza as keys
    for i in range(len(keys)):
        for j in range(len(keys) - (1 + i)):
            if keys[j] > keys[j+1]:
                    keys[j], keys[j+1] = keys[j+1], keys[j]                

    #Então coloca os na lista que vai ser devolvida
    lista = []
    for i in range(len(keys)):
        for j in dicionario:
            if j == keys[i]:
                for k in range(len(dicionario[j])):
                    lista.append(dicionario[j][k])

    return lista


def rawDataHora(data, hora):
    if data and hora:
        return int(data[6:] + data[3:5] + data[0:2] + hora[0:2] + hora [3:5])
    elif data:
        #Caso só tenha data, a hora fica acima do limite
        return int(data[6:] + data[3:5] + data[0:2] + "2401")
    elif hora:
        #Caso só tenha hora, a data fica acima do limite
        return int("100000000" + hora[0:2] + hora[3:5])
    #Caso não tenha nada, a hora fica acima do limite de ambas
    return 1000000002402

def rawPrio(prio):
    if prio:
        return prio[1].upper()
    return "|"
   

########################VALIDAÇÃO########################

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
            #Achei mais interessante que fazer manualmente
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

        #Checagem dos dias no mês
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


########################UTILIDADES########################

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


def prepararItem(item):

    desc = item[0].strip()
    extras = item[1]
    
    data = extras[0]
    hora = extras[1]
    prio = extras[2].upper()
    cont = extras[3]
    proj = extras[4]

    if  len(desc) > 1:
        desc = desc[0].upper() + desc[1:]
    else:
        desc = desc.upper()
    if data:
        data = data[0:2] + "/" + data[2:4] + "/" + data[4:]        
    if hora:
        hora = hora[0:2] + "h" + hora[2:] + "m"

    return [data, hora, prio, desc, cont, proj]

def limparTela():
    
    print("\n"*50)


def limparLista(lista):

    listaFinal = []
    while lista:
        item = lista.pop(0).strip()
        if item:
            listaFinal.append(item)
    return listaFinal


########################EXECUÇÃO########################





arquivo_TODO = "todo.txt"
arquivo_DONE = "done.txt"

teste = "11092005 descricao descricao 0911 (A) 1102 @contexto 1102 descartar +projeto +projeto2"
teste2 = "11092005 (B) 0911 11092005 (A) +projeto descricao 1102 +projeto2"

print(teste)
print(prepararItem(organizar(teste.split(" "))))
print()
print(prepararItem(organizar(teste.split(" "), False)))

print("\n")
print(teste2)
print(prepararItem(organizar(teste2.split(" "))))
print()
print(prepararItem(organizar(teste2.split(" "), False)))

print("\n\n")
arquivo = lerArquivo()
itens = []
for i in range(len(arquivo)):
    itens.append(prepararItem(arquivo[i]))

itens = ordenar(itens)

for i in range(len(itens)):
    print(itens[i])

#processarComandos(["teste", "A+", "teste", "teste2"])
#processarComandos(sys.argv)

#while printCores(strItem(organizar(input("ORGANIZAR: ").split(" "))), "RED"):
#    pass
