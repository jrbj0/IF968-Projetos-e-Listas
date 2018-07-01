def elem(c, texto):
    if texto:
        if texto[0] == c:
            return True
        return elem(c, texto[1:])
    return False


def pegaPalavra(texto, separar):
    if texto and separar:
        if elem(texto[0], separar):
            return ""
        return texto[0] + pegaPalavra(texto[1:], separar)
    return texto


def pegaResto(texto, separar):
    if texto and separar:
        if elem(texto[0], separar):
            return texto
        return pegaResto(texto[1:], separar)
    return ""


def tiraSeparadores(texto, separar):
    if texto:
        if separar:
            if elem(texto[0], separar):
                return tiraSeparadores(texto[1:], separar)
            return texto
        return texto
    return ""


def tokenizar(texto, separar):
    if texto:
        if separar:
            texto = tiraSeparadores(texto, separar)
            palavra = pegaPalavra(texto, separar)
            resto = pegaResto(texto, separar)            
            return [palavra] + tokenizar(resto, separar)
        return [texto]
    return []
    
print(tokenizar("(81)123-456-789", "()-"))


##########################################################################


def somaLinhas(linha1, linha2):
    if len(linha1) == len(linha2):
        if linha1:
            return [linha1.pop(0) + linha2.pop(0)] + somaLinhas(linha1, linha2)
        return []
    raise BaseException("As linhas tem tamanhos diferentes!")


def somaMatrizes(matriz1, matriz2):
    if len(matriz1) == len(matriz2):
        if matriz1:
            return [matriz1.pop(0) + matriz2.pop(0)] + somaMatrizes(matriz1, matriz2)
        return []
    raise BaseException("As matrizes tem tamanhos diferentes!")


def menor(elementos):
    if len(elementos) == 1:
        return elementos[0]
    return menorAux(elementos[0], elementos)


def menorAux(menorElemento, elementos):
    if elementos:
        if elementos[0] < menorElemento:
            return menorAux(elementos[0], elementos[1:])
        return menorAux(menorElemento, elementos[1:])
    return menorElemento


def remover(e, elementos):
    if elementos:
        if e == elementos[0]:
            return elementos[1:]
        return [elementos[0]] + remover(e, elementos[1:])
    return elementos


def ordenar(elementos):
    if elementos:
        menorElemento = menor(elementos)
        elementos = remover(menorElemento, elementos)
        return [menorElemento] + ordenar(elementos)
    return []

print(ordenar([8, 5, 12, 6, 10, 4]))
