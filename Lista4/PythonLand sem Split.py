# João Rafael

#Método para separar a string em listas manualmente
def separar_string(texto, separador):
    
    palavra = ""
    lista = []
    i = 0
    for i in range(0, len(texto)):

        #Checa todas as letras do texto pelo separador
        letra = texto[i]        
        if letra != separador:
            #E forma elas novamente
            palavra = palavra + letra

        #Quando encontra o separador, adiciona a palavra à lista 
        else:
            lista.append(palavra)
            palavra = ""

    #Como não tem um separador no final do texto
    #Sobra essa última palavra fora da lista
    #Que então é adicionada à lista
    lista.append(palavra)
            
    #E por fim a lista é devolvida
    return lista


        
print("Nome Força,Habilidade,Inteligência,Sabedoria",       
      "Característica1,Característica2",                    
      "Habilidade1,Habilidade2 (Repetir para cada monstro)")                            

#O input contendo todos os monstros
monstrosString = input()

#Usa o método de separar_string para criar a lista onde tem todos monstros
monstrosLista = separar_string(monstrosString, " ")

bestiario = []
m = 0
#Note o passo 4 no final, é um for que faz "i + 4" a cada laço
for i in range(0, len(monstrosLista), 4):

    #Pega o primeiro item e atribui a nome
    nome = monstrosLista[i]

    #Separa o segundo item em uma lista e atribui a Stats usando o separar_string	
    stats = monstrosLista[i+1]
    stats = separar_string(stats, ",")

    #E depois as características
    caracteristicas = monstrosLista[i+2]                    
    caracteristicas = separar_string(caracteristicas, ",")            

    #Então as habilidades
    habilidades = monstrosLista[i+3]                        
    habilidades = separar_string(habilidades, ",")                    

    #Assim todos os 4 itens são tratados e colocados na lista monstro
    monstro = [nome, stats, caracteristicas, habilidades]

    print(monstro)

    #E finalmente o Monstro é colocado no bestiário
    bestiario.append(monstro)



    #Se esse for o fim do input, OK
    #Se não, o laço é repetido com os próximos 4 itens


    
    #Toda essa parte é só para mostrar os dados do monstro
    #O bestiário é acessado usando a variável m
    #Que foi criada lá no começo só para esse motivo
    #---
    print("\n\nCriatura:\t\t", bestiario[m][0])
    print("Força:\t\t\t",  bestiario[m][1][0],
          "\nHabilidade:\t\t",  bestiario[m][1][1],
          "\nInteligência\t\t",  bestiario[m][1][2],
          "\nSabedoria:\t\t",  bestiario[m][1][3])
    
    caracString = ""                                        
    for x in range(0, len(bestiario[m][2])):                
        caracString = caracString + bestiario[m][2][x]+ " " 

    print("Caracteristicas:\t", caracString)                

    habilString = ""                                        
    for x in range(0, len(bestiario[m][3])):                
        habilString = habilString + bestiario[m][3][x]+ " "   

    print("Habilidades:\t\t",  habilString)
    #---
    

    #Finalmente o m é incrementado e o laço repete (ou não)
    print("\n\n")
    m = m+1                                                 

    
print("\n\n")                                             
print(bestiario)
