#João Rafael

def menu(estoque):
    limparTela()
    print("Escolha uma das opções abaixo para continuar:\n" +
          "1. Comprar Produtos\n" +
          "2. Abastecer Estoque\n" +
          "3. Checar Estoque\n" +
          "4. Cadastrar Produtos\n" +
          "5. Remover Produto\n" +
          "6. Finalizar\n")

    escolha = 0
    opcoes = {1: comprar, 2: abastecer, 3: checar, 4: cadastrar, 5: remover}
    while escolha not in range(1, len(opcoes) + 2):
        escolha = input("Opção: ")
        if escolha.isdigit():
            escolha = int(escolha)

    if escolha in opcoes:
        opcoes[escolha](estoque)


#Função que interpreta o texto, produzindo uma lista com os atributos dos produtos
#Serve tanto para cadastrar, quanto para abastecer e comprar
def lerProdutos(texto, cadastrar):

    ###############################################################
    if texto == "teste":
        texto = "Ketchup 3.50 10, Maionese 4.00 7, Abacaxi 8.00 5"
    if texto == "teste2":
        texto = "Ketchup 10, Maionese 7, Abacaxi 5"
    if texto == "teste3":
        texto = "Ketchup 5, Maionese 3, Abacaxi 2"
    if texto == "teste4":
        texto = "Ketchup 20, Maionese -12, Abacaxi 5"
    ###############################################################

    texto = texto.strip().upper()
    texto = texto.split(", ")

    n = 1
    if cadastrar:
        n = 2

    produtos = []
    if texto:
        for i in range(len(texto)):
            produto = texto[i].split(" ")
            if len(produto) > n and len(produto) < n + 2:
                produtos.append(cadastrar_ou_abastecer(produto, cadastrar))
    return produtos

#Função que diferencia o append entre as operações
def cadastrar_ou_abastecer(texto, cadastrar):
    if cadastrar:
        return [texto[0], float(texto[1]), int(texto[2])]
    else:
        return [texto[0], 0.0, int(texto[1])]


#Função que interpreta a lista produzida pela lerProdutos
def lerLista(lista, cadastrar):

    estoque = {}
    if lista:
        for i in range(len(lista)):
            if cadastrar:
                if lista[i][1] < 0:
                    lista[i][1] = 0
                estoque[lista[i][0]] = [lista[i][1], lista[i][2]]

            else:
                estoque[lista[i][0]] = [0.0, lista[i][2]]

    if estoque == {}:
        print("\n\n\n\n\nOPERAÇÃO FALHOU!\n\n\n")
        input("\n" * 5 + "Insira qualquer coisa para continuar\n")

    return estoque


def comprar(estoque):

    print("\nInsira os itens que deseja comprar no formato: \nNOME QUANTIDADE, NOME QUANTIDADE\n")
    texto = input()

    remover = []
    if texto:
        limparTela()
        produtos = lerLista(lerProdutos(texto, False), False)
        for i in produtos:
            if i in estoque:
                if produtos[i][1] < 0:
                    produtos[i][1] = 0
                elif produtos[i][1] > 0:
                    print("\n" + i, "\nQuantidade no estoque:", str(estoque[i][1]),
                          "\nQuantidade a comprar:", str(produtos[i][1]),
                          "\nPreço unitário:", reais(estoque[i][0]),
                          "\nPreço total:", reais(estoque[i][0] * produtos[i][1]))

                    if produtos[i][1] > estoque[i][1]:
                        print("\nQUANTIDADE INSUFICIENTE EM ESTOQUE!!!\n")
                        remover.append(i)
                    else:
                        produtos[i][0] = estoque[i][0]
                        estoque[i][1] -= produtos[i][1]

            else:
                print(i, "não foi encontrado!")
                remover.append(i)

        for i in range(len(remover)):
            produtos.pop(remover[i])

        if produtos:
            print("\nDeseja comprar os produtos listados?")
            if simNao():
                estoque.update(produtos)
        else:
            print("\n\n\n\nNENHUM PRODUTO FOI COMPRADO!\n\n\n")
            input("\n" * 5 + "Insira qualquer coisa para continuar\n")
    menu(estoque)


def abastecer(estoque):

    print("\nInsira os itens que deseja abastecer no formato: \nNOME QUANTIDADE, NOME QUANTIDADE\n")
    texto = input()

    remover = []
    if texto:
        limparTela()
        produtos = lerLista(lerProdutos(texto, False), False)
        for i in produtos:
            if i in estoque:
                print("\n" + i, "\nPreço:", reais(estoque[i][0]), "\nQuantidade:", str(estoque[i][1]),"+", str(produtos[i][1]))
                produtos[i][0] = estoque[i][0]
                produtos[i][1] += estoque[i][1]

            else:
                print(i, "não está cadastrado!")
                remover.append(i)

        for i in range(len(remover)):
            produtos.pop(remover[i])

        if produtos:
            print("\nDeseja abastecer os produtos listados?")
            if simNao():
                estoque.update(produtos)
        else:
            print("\n\n\n\nNENHUM PRODUTO FOI ABASTECIDO!\n\n\n")
            input("\n" * 5 + "Insira qualquer coisa para continuar\n")
    menu(estoque)


def checar(estoque):

    limparTela()
    if estoque:
        for i in estoque:
            print("\n" + i, "\nPreço:", reais(estoque[i][0]), "\nQuantidade:", str(estoque[i][1]))
    else:
        print("O ESTOQUE ESTÁ COMPLETAMENTE VAZIO!!!")

    input("\n" * 5 + "Insira qualquer coisa para continuar\n")
    menu(estoque)


def cadastrar(estoque):

    print("\nInsira os itens que deseja cadastrar ou alterar no formato: \nNOME PREÇO QUANTIDADE, NOME PREÇO QUANTIDADE\n")
    texto = input()
    if texto:
        produtos = lerLista(lerProdutos(texto, True), True)
        for i in produtos:
            print("\n" + i, "\nPreço:", reais(produtos[i][0]),
                  "\nQuantidade:", str(produtos[i][1]))

        if produtos:
            print("\nDeseja inserir os produtos listados?")
            if simNao():
                estoque.update(produtos)
    menu(estoque)


def remover(estoque):
    print("\nInsira o nome do item que deseja remover:")
    i = input().upper()
    if i in estoque:
        print("\n" + i, "\nPreço:", reais(estoque[i][0]), "\nQuantidade:", str(estoque[i][1]))
        print("\n\nRealmente deseja remover", i + "?")

        if simNao():
            estoque.pop(i)
    else:
        print("\n\nPRODUTO NÃO ENCONTRADO!\n")
        input("\n" * 2 + "Insira qualquer coisa para continuar\n")
    menu(estoque)



#Utilidades
def limparTela():
    print("\n"*50)

def reais(numero):
    return "R$" + format(numero, ".2f")

def simNao():
    Sims = ["S", "SI", "SIM", "Y", "YE", "YES"]
    Naos = ["N", "NA", "NAO", "NÃ", "NÃO", "NO"]
    while True:
        escolha = input("   (S)im ou (N)ão: ").upper()
        if escolha in Sims:
            return True
        elif escolha in Naos:
            return False

#############################

print("Comece inserindo os produtos iniciais...")
x = 0
estoque = {}
estoque = cadastrar(estoque)
   
