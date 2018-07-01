#João Rafael

def estaOrdenada(lista):
    if lista:
        if auxOrdenada(lista[0], lista[1:]):
            return estaOrdenada(lista[1:])
        return False
    return True

def auxOrdenada(num, numeros):
    if numeros:
        if num <= numeros[0]:
            return True
        return False
    return True

def palindromo(palavra):
    palavra = palavra.lower()
    return palavra == inverter(palavra, "")

def inverter(palavra, resultado):
    if palavra:
        return inverter(palavra[1:], palavra[0] + resultado)
    return resultado

def removerIntermediarios(frase):
    if frase:
        if elem(frase[0], " ,.!?-;:"):
            return removerIntermediarios(frase[1:])
        frase = frase[0] + removerIntermediarios(frase[1:])           
    return frase.lower()

def elem(c, texto):
    if texto:
        if texto[0] == c:
            return True
        return elem(c, texto[1:])

def numPaginas(limite, contador = 1, digitos = ""):
    if len(digitos) < limite:
        return numPaginas(limite, contador + 1, digitos + str(contador))
    return contador - 1
    


print("1.")
print("estaOrdenada([1,2,3,4,5]) = ", estaOrdenada([1,2,3,4,5]))
print("estaOrdenada([5,4,3,2,1]) = ", estaOrdenada([5,4,3,2,1]))
print("estaOrdenada([3,2,1,4,5]) = ", estaOrdenada([3,2,1,4,5]))

print("\n2.")
print("palindromo('Arara') =", palindromo("Arara"))
print("palindromo('ararinha') =", palindromo("ararinha"))
print("palindromo('True') =", palindromo("esse ultimo capítulo de one punch man foi bem legal"))

print("\n3.")
print("removerIntermediarios('A mala nada na lama.')\n>", removerIntermediarios("A mala nada na lama."))
print("removerIntermediarios('Acata o danado... e o danado ataca!')\n>", removerIntermediarios("Acata o danado... e o danado ataca!"))

print("\npalindromo(removerIntermediarios('A mala nada na lama.'))\n>", palindromo(removerIntermediarios('A mala nada na lama.')))

print("\n4.")
print("numPaginas(13) =",numPaginas(13))
print("numPaginas(21) =",numPaginas(21))
print("numPaginas(192) =",numPaginas(192))
print("numPaginas(1578) =",numPaginas(1578))
