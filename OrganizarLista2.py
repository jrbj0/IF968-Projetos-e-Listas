lista1 = [312, 4, 6, 6, 74, 25, 13, 8, 5, 500, 10]
lista2 = [8, 5445, 6, 24, 46, 25, 25, 66, 1]

lista1 = lista1 + lista2
lista2 = []


for i in range(0, len(lista1)):

    adicionar = True
    for x in range(0, len(lista2)):
        if lista1[i] == lista2[x]:
            adicionar = False

    if adicionar:
        lista2.append(lista1[i])


for i in range(0, len(lista2)):

    for x in range(i, len(lista2)):
        
        if lista2[i] > lista2[x]:
            lista2[x], lista2[i] = lista2[i], lista2[x]





###Eis uma forma bem mais prática de remover duplicatas
###O problema é que eu não tenho certeza se Castor deixaria usar
##
##for i in range(0, len(lista1)):
##
##    if lista1[i] not in lista2:
##        lista2.append(lista1[i])
