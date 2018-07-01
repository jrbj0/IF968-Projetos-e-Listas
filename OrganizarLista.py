#João Rafael

listaInput1 = [4, 6, 74, 12, 25, 12, 13, 12, 8, 12, 5]
listaInput2 = [12, 21, 1, 1, 65, 8, 46, 25, 66, 5, 13]
listaDesordenada = listaInput1 + listaInput2
listaFinal = []

for i in range(0, len(listaDesordenada)): 

    adicionar = True    
    for iigual in range(0, len(listaFinal)):            
       if listaDesordenada[i] == listaFinal[iigual]:
           adicionar = False

    if adicionar:
        listaFinal.append(listaDesordenada[i])


for i in range(0, len(listaFinal)):

    numero = listaFinal[i]

    for imenor in range(0, len(listaFinal)):
        if numero < listaFinal[imenor]:
            numero = listaFinal[imenor]
            listaFinal[imenor] = listaFinal[i]
            listaFinal[i] = numero
        
        

print(listaFinal)
        
                
                
              



