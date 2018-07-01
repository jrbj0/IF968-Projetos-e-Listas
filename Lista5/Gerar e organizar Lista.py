#João Rafael

from random import randint
from time import clock

def gerarLista(tamanho):
    lista = []
    i = 0
    while i < tamanho:
        numero = randint(-100, 100)
        if numero not in lista:
            lista.append(numero)
            i += 1
    return lista

def organizarCrescente(lista):
    for i in range(len(lista)):
        for x in range(i, len(lista)):
            if lista[i] > lista[x]:                
                lista[x], lista[i] = lista[i], lista[x] 
    return lista

def organizarDecrescente(lista):
    for i in range(len(lista)):
        for x in range(i, len(lista)):
            if lista[i] < lista[x]:                
                lista[x], lista[i] = lista[i], lista[x] 
    return lista

def lerLista(lista):
    texto = ""
    for i in range(len(lista)):
        texto += str(lista[i])
        if i < len(lista) - 1:
            texto += ", "
    return texto
    
#---


tamanhoLista = 0
while tamanhoLista < 10 or tamanhoLista > 100:
    tamanhoLista = int(input("Informe o tamanho da lista: "))

ordem = ""
while ordem != "C" and ordem != "D":
    ordem = input("Selecione a opção de ordenação: (C)rescente ou (D)ecrescente? ").upper()

tempo = clock()

listaFinal = gerarLista(tamanhoLista)
textoLista = lerLista(listaFinal)
print("\n1) Lista original:", textoLista)

if ordem == "C":
    listaFinal = organizarCrescente(listaFinal)
    parteTexto = "crescente"
else:
    listaFinal = organizarDecrescente(listaFinal)
    parteTexto = "decrescente"

textoLista = lerLista(listaFinal)
print("\n2) Lista ordenada", parteTexto + ":", textoLista)

tempo = clock() - tempo
print("\n3) Tempo de execução da ordenação:", str(tempo), "s")



