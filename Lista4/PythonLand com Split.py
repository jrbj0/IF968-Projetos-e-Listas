# João Rafael

# Lista que conterá todos os monstros
bestiario = []

# "m" aqui serve para contabilizar a quantidade de items na lista "bestiario"
m = 0                                                       

print("Nome Força,Habilidade,Inteligência,Sabedoria",       
      "Característica1,Característica2",                    
      "Habilidade1,Habilidade2")                            

# "monstrosLista" recebe o input e o separa como uma lista através do método split()
# O split() transforma uma string em uma lista cujo seus elementos são todos os caracteres após o caractere informado nos parâmetros
monstrosString = input()                                    
monstrosLista = monstrosString.split(" ")                   


# Aquele 4 no final indica o passo do laço
# Ou seja, a cada execução do for o i vai aumentar em 4 unidades
for i in range(0, len(monstrosLista), 4):


    # O primeiro item da lista "monstrosLista", formada pelo split(), é atribuido à variável "nome"
    nome = monstrosLista[i]
	
    # Atribui o segundo item da lista "monstrosLista" à variável "stats"
    # Transforma a string "stats" em uma lista que contém os valores da string sem as vírgulas
    # "stats" será uma lista que contém valores que correspondentes à força, à habilidade, à inteligência e à sabedoria
    stats = monstrosLista[i+1]                              
    stats = stats.split(",")                                

    # Atribui o terceiro item da lista "monstrosLista" à variável "caracteristicas"
    # e repete o tratamento realizado anteriormente
    caracteristicas = monstrosLista[i+2]                    
    caracteristicas = caracteristicas.split(",")            

    # Atribui o quarto item da lista "monstrosLista" à variável "habilidades" 
    # e repete o tratamento anterior
    habilidades = monstrosLista[i+3]                        
    habilidades = habilidades.split(",")                    

    # Junta todos os valores em uma lista chamada "monstro"
    monstro = [nome, stats, caracteristicas, habilidades]

    # Adiciona monstro na lista "bestiario"
    bestiario.append(monstro)                               

	
    # Esta parte é imprime os dados do monstro que foi adicionado
    print("\n\nCriatura:\t\t", bestiario[m][0])	            # Imprime o item 0 (Nome) da lista "monstro" no índice "m" da lista "bestiario"

    print("Força:\t\t\t",  bestiario[m][1][0],              # Imprime o item 0 (Força) da lista "stats" no índice "1" da lista "monstro" (stats) no índice "m" da lista "bestiario"
          "\nHabilidade:\t\t",  bestiario[m][1][1],         # Imprime o item 1 (Habilidade) da lista "stats" no índice "1" da lista "monstro" (stats) no índice "m" da lista "bestiario"
          "\nInteligência\t\t",  bestiario[m][1][2],        # Imprime o item 2 (Inteligência) da lista "stats" no índice "1" da lista "monsto" (stats) no índice "m" da lista "bestiario"
          "\nSabedoria:\t\t",  bestiario[m][1][3])          # Imprime o item 3 (Sabedoria) da lista "stats" no índice "1" da lista "monstro" (stats) no índice "m" da lista "bestiario"

    # Esta parte serve simplesmente para imprimir os itens da lista
    # Se der print em uma lista, ela devolve "['texto1', 'texto2', 'texto3']"
    # Porém a questão quer que devolva "texto1 texto2 texto3"
    caracString = ""                                        
    for x in range(0, len(bestiario[m][2])):                
        caracString = caracString + bestiario[m][2][x]+ " " 

    print("Caracteristicas:\t", caracString)                

    habilString = ""                                        
    for x in range(0, len(bestiario[m][3])):                
        habilString = habilString + bestiario[m][3][x]+ " "   

    print("Habilidades:\t\t",  habilString)                 

    print("\n\n")
    m = m+1                                                 

#Como está em um for, vai repetir até acabarem os monstros do input
#Caso só tenha 1 monstro, finaliza o laço
    
print("\n\n\n")                                             
print(bestiario)
