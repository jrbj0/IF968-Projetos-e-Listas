#Joao Rafael

lista = []
for i in range(0, 24):

    num = input(str(i + 1) + ": ")

    if num == "":
        break
    
    num = int(num)    
    lista.append(num)



soma = 0
maiornum = lista[0]
menornum = lista[0]
for i in range(0, len(lista)):

    num = lista[i]
    soma = soma + num
    
    if num > maiornum:
        maiornum = num

    if num < menornum:
        menornum = num

media = soma / len(lista)
media = format(media, '.4f')

print("Soma dos itens da lista:\t\t", soma)
print("Media dos itens da lista:\t\t", media)
print("Maior item da lista:\t\t\t", maiornum)
print("Menor item da lista:\t\t\t", menornum)
    
    

    

