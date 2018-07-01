def palindromo(texto):
    if texto.lower() == contrario(texto.lower()):
        return True
    else:
        return False

def contrario(texto, resultado = ""):
    if len(texto) > 0:
        return contrario(texto[1:], texto[0] + resultado)
    else:
        return resultado

print(palindromo("omississimo"))




def raizQuadrada(numero, resposta, diferenca):
    potencia = numero * numero
    if potencia > numero:
        if potencia > resposta - diferenca and potencia < resposta + diferenca:
            print(numero, "é a raiz de", resposta)
        else:
            return raizQuadrada((resposta/numero + numero) / 2, resposta, diferenca)
    else:
        print("não conseguiu")

raizQuadrada(100, 100, 5)




def subPalindromo(texto, resposta = ""):
    texto = texto.lower()
    if palindromo(texto):
        if len(texto) > len(resposta):
            return texto
    if len(texto) > 1:
        if len(checar(texto)) > len(resposta):
            resposta = checar(texto)
        return subPalindromo(texto[1:], resposta)
    else:
        return resposta

def checar(texto):
    texto = texto.lower()
    if palindromo(texto):
        return texto
    else:
        if len(texto) > 1:
            if palindromo(texto):
                return texto
            else:
                return checar(texto[:-1])
        else:
            return texto

print(subPalindromo("Fernando"))
    

