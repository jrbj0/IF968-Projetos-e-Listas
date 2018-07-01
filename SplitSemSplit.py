
entrada1 = "medusa 0,0,0,0 monstro petrificar"
entrada2 = "medusa 0,0,0,0 monstro petrificar minotauro 200,1,1,1 monstro mugido,chifrada"



entrada1 = entrada1
entrada2 = entrada2


def splitbosta(entrada, splitador):
    campo = ""
    resultado = []
    i = 0
    while i < len(entrada):
        c = entrada[i]
        if c != splitador:
            campo = campo + c
        elif i == len(resultado) - 1:
            resultado.append(campo)
        else:
            resultado.append(campo)
            campo = ""

        i = i + 1

    if campo:
        resultado.append(campo)

    return resultado

lista = splitbosta(entrada2, " ")



listamenor = []
listacompleta = []
listamonstros = []

for x in range(0, len(lista), 4):
    monstro = []    
    for i in range(0, len(lista)):    
        listacompleta.append(splitbosta(lista, ","))

    for z in range(x, x + 4):
        listamonstros.append(listacompleta[z])

print(listacompleta[0])
    
    
    
