def entreOsMaiores(lista):

    indice1, indice2 = 0, 0
    for i in range(len(lista)):
        if lista[i] > lista[indice1]:
            if lista[i] > lista[indice2]:
                indice2 = i
            else:
                indice1 = i

    listafinal = []
    if indice1 != indice2:
        for i in range(indice2 + 1, indice1):
            listafinal.append(lista[i])

    return listafinal    

print(entreOsMaiores([3,2,10,4,3,7,5]))

print("\n" * 10)




def substring(string, sub):
    indices = []
    for i in range(len(string) - (len(sub) - 1)):
        palavra = ""
        for x in range(len(sub)):
            palavra += string[i + x]
        if palavra == sub:
            indices.append(i)
    return indices

print(substring("abcdefcdxywedgccd","cd"))

print("\n" * 10)




def potenciar(num, potencia):
    i = 0
    numero = 1
    while i != potencia:
        numero = numero * num
        i += 1
    return numero

print(potenciar(12, 4))

print("\n" * 10)





def somarMatrizes(lista1, lista2):
    listafinal = []
    for i in range(len(lista1)):
        lista = []
        for x in range(len(lista1[i])):
            lista.append(lista1[i][x] + lista2[i][x])
        listafinal.append(lista)
    return listafinal

print(somarMatrizes([[2,1,3], [3,2,1], [1,2,3]], [[5,7,9], [4,3,2], [9,9,9]]))
        




def multiplicarMatrizes(lista1, lista2):
    listafinal = []
    for i in range(len(lista1)):
        lista = []
        for x in range(len(lista1[i])):
            if x+1 <= len(lista1[i]):
                print("NÃO TERMINEI SA BAGAÇA")
    







