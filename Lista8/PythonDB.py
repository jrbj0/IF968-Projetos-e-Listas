# João Rafael

def menu():

    dados = []
    while not dados:
        
        limparTela()
        print("MENU PRINCIPAL DO BANCO DE DADOS",
              "\nEscolha a operação que deseja realizar:",
              "\n1. Registrar Pessoa",
              "\n2. Procurar Pessoa",
              "\n3. Alterar Registro",
              "\n4. Deletar Registro",
              "\n5. Finalizar")

        switch = {1: "create",
                  2: "read",
                  3: "update",
                  4: "delete",
                  5: "sair"}

        opcao = ""
        while not opcao:
            opcaoinput = input("\nOperação: ")
            if opcaoinput.isdigit():
                if int(opcaoinput) <= len(switch) and int(opcaoinput) > 0:
                    opcao = switch[int(opcaoinput)]
                    if opcao == "sair":
                        return ""

        limparTela()
        dados = formatoEntrada(opcao)

    resultado = (crud(opcao, dados))
    if resultado:
        input("\n" + resultado)   

    return opcao


def criarArquivo(caminho):

    f = open(caminho, "a+")
    f.seek(0)
    if not f.readlines():
        f.write("Nome Sobrenome Idade Sexo\n")
    f.close()
    

def lerArquivo(f):

    lista = []
    linhas = f.readlines()
    for i in range(1, len(linhas)):
        linha = limparTexto(linhas[i])
        if linha:
            lista.append(linha.split(" "))
    return lista


def escreverArquivo(linhas, caminho, operacao):

    criarArquivo(caminho)    
    f = open(caminho, operacao)
    for i in range(len(linhas)):
        f.write("\n")
        for j in range(len(linhas[i])):
            f.write(linhas[i][j] + " ")
        f.write("\n")
    f.close

def alterarArquivo(linhas, caminho):

    criarArquivo(caminho + "temp")
    escreverArquivo(linhas, caminho + "temp", "a+")

    from os import rename, remove
    remove(caminho)
    rename(caminho + "temp", caminho)


def formatoEntrada(operacao):

    textoOperacao = "registrar uma pessoa"
    if operacao == "delete":
        textoOperacao = "deletar um registro"
    textoPrint = "Para " + textoOperacao + ", insira os dados da forma abaixo:"
    textoInput = "NOME SOBRENOME IDADE (M ou F)\n"
    
    updateInput = ""
    if operacao == "sair":
        return "sair"    
    elif operacao == "read":
        readInput = input("Para buscar um registro, digite o Nome e/ou Sobrenome da pessoa\n")
        return limparTexto(readInput)    
    elif operacao == "update":
        print("Para editar um registro, digite os dados que deseja editar da forma abaixo:")
        updateInput = tratarDados(receberInput(textoInput))        
        if updateInput:
            textoPrint = "\nAgora digite os dados novos no mesmo formato"
        else:
            textoPrint = ""

    dados = ""
    if textoPrint:
        print(textoPrint)
        dados = tratarDados(receberInput(textoInput))
        
    if updateInput and dados:
        return [updateInput, dados]
    else:
        return dados


def tratarDados(lista):

    lista = capitalizarLista(lista)
    if len(lista) == 4 and lista[2].isdigit() and len(lista[3]) == 1:
        return lista
    else:
        input("\nFORMATO INVÁLIDO!")

        
def receberInput(inputTexto):

    texto = input(inputTexto)
    texto = texto.split(" ")
    for i in range(len(texto)):
        texto[i] = limparTexto(texto[i])    
    return texto


def crud(operacao, dados):
    
    switch = {"create": create,
              "read": read,
              "update": update,
              "delete": delete}
    resultado = switch[operacao](dados)
    
    return resultado

    
def create(dados):

    linha = ""
    for i in range(len(dados)):
        linha += dados[i] + " "
    linha = linha[0:-1]
    
    escreverArquivo([[linha]], caminho, "a+")

    input("\n" + dados[0] + " " + dados[1] + " adicionado ao banco de dados!")


def read(dados):

    banco = lerArquivo(open(caminho, "r"))

    pessoa = ""
    if banco:    
        for i in range(len(banco)):
            for j in range(2):
                if dados.upper() == banco[i][j].upper():
                    for k in range(len(banco[i])):
                        pessoa += limparTexto(banco[i][k]) + " "
                    pessoa = pessoa[0:-1] + "\n"                

    if pessoa:
        return pessoa
    else:
        input("\n" + dados + " não foi encontrado!")


def update(dados):
    banco = lerArquivo(open(caminho, "r"))

    dadosAntes = dados[0]
    dadosDepois = dados[1]

    alterado = ""
    if banco:
        i = 0
        while i < len(banco):
            if banco[i] == dados[0]:
                alterado = banco[i] = dados[1]
            i += 1

    if alterado:
        alterarArquivo(banco, caminho)
        input("\n" + dados[0][0] + " " + dados[0][1] +
              " alterado para " + dados[1][0] + " " + dados[1][1])
    else:
        input("\n" + dados[0][0] + " " + dados[0][1] + " não encontrado!")
        

def delete(dados):
    banco = lerArquivo(open(caminho, "r"))

    deletado = ""
    if banco:
        i = 0
        while i < len(banco):
            if banco[i] == dados:
                deletado = banco.pop(i)
            i += 1

    if deletado:
        alterarArquivo(banco, caminho)
        input("\n" + dados[0] + " " + dados[1] + " deletado do banco de dados!")



def limparTela():
    print("\n"*50)

def limparTexto(texto):
    texto = texto.replace("\n", "")
    texto = texto.strip()
    return texto

def capitalizarLista(lista):

    for i in range(len(lista)):
        if len(lista[i]) > 1:
            lista[i] = lista[i][0].upper() + lista[i][1:].lower()
        else:
            lista[i] = lista[i].upper()            
    return lista       

def simNao():
    Sims = ["S", "SI", "SIM", "Y", "YE", "YES", "1"]
    Naos = ["N", "NA", "NAO", "NÃ", "NÃO", "NO", "0"]
    while True:
        escolha = input("   (S)im ou (N)ão: ").upper()
        if escolha in Sims:
            return True
        elif escolha in Naos:
            return False


caminho = "data.txt"
criarArquivo(caminho)

while menu():
    pass
    
