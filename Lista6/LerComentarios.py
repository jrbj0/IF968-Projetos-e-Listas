#João Rafael

def lerArquivo(caminho):

    f = open(caminho)
    linhas = f.readlines()
    f.close()


    texto = []
    printar = ""
    for i in range(len(linhas)):

        printar += linhas[i]

        linhas[i] = linhas[i].strip()
        linhas[i] = linhas[i].replace("\n", "").replace('"', "")

        palavra = ""
        for j in range(len(linhas[i])):

            c = linhas[i][j]

            if c != " " and c != "," and c != ".":
                palavra = palavra + c
            else:
                if palavra:
                    texto.append(palavra)
                    palavra = ""
        if palavra:
            texto.append(palavra)

    return texto, printar

def contabilizarComentarios(texto, positivos, negativos):

    palavras = 0
    positividade = 0
    for i in range(len(texto)):
        
        if texto[i].lower() in positivos:            
            palavras += 1
            positividade += 1
            
        elif texto[i].lower() in negativos:
            palavras += 1

    return palavras, positividade

######

print("O PROGRAMA VAI LER DEFINIR OS COMENTÁRIOS POSITIVOS E NEGATIVOS")
print("DE ACORDO COM OS ARQUIVOS 'positivos.txt' e 'negativos.txt'")

continuar = True
arquivo = "comentarios.txt"

while arquivo:

    arquivo = input("FAVOR INSIRA O NOME DO ARQUIVO E SUA  QUE VOCÊ DESEJA LER:\n")
   
    if arquivo:
        positivos, x = lerArquivo("positivos.txt")
        negativos, x = lerArquivo("negativos.txt")

        comentarios, printar = lerArquivo(arquivo)
        print("\n\n" + printar)
        
        qtdPalavras, qtdPositivos = contabilizarComentarios(comentarios, positivos, negativos)

        porcentagem = int((qtdPositivos / qtdPalavras) * 100)
        print(str(porcentagem) + "% de positividade\n")

        print("\nCASO DESEJE PARAR, INSIRA ''")
        arquivo = "."
            
            
            

    
            
    
