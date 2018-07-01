#João Rafael

def listarPrimos(limite):
    primos = [2]
    tentativas = 0
    for i in range(3, int((limite ** 0.5))):
        
        x = 0
        primo = True
        while primos[x] < len(primos):
            if i % primos[x] == 0 and primo:
                primo = False
            x += 1
            tentativas += 1
        
        if primo:
            primos.append(i)            

    return primos, tentativas

def fatorar(numero, primos, resultados, tentativas):

    primo = False
    if numero in primos:
        resultados.append(int(numero))
        primo = True
    elif numero ** 0.5 in primos:
        resultados.append(int(numero ** 0.5))
        primo = True

    i = 0    
    while i < len(primos) and not primo:            
        if numero % primos[i] == 0:
            resultados.append(primos[i])
            numero = numero / primos[i]
            resultados, numero, tentativas = fatorar(numero, primos, resultados, tentativas)
            primo = True        
        i += 1
        tentativas += 1
    
    if not resultados or (len(resultados) == 1):
        resultados = []
        
    return resultados, numero, tentativas


##############



from time import clock

while True:

    numero = 0    
    print("\nDIGITE 1 CASO DESEJE PARAR")
    while numero < 1:
        numero = int(input("INSIRA UM NÚMERO PARA FATORAR: "))        
    if numero == 1:
        break
    
    tempo = clock()
    
    primos, tentativasLista = listarPrimos(numero)
    resultados, numero, tentativasFatoracao = fatorar(numero, primos, [], 0)
    resultados.append(int(numero))
    
    tempo = clock() - tempo

    if len(resultados) > 1:
        texto = str(resultados[0])

        for i in range(1, len(resultados)):
            if i != len(resultados):
                texto += " * "
            texto += str(resultados[i])
    else:
        texto = "PRIMO!"

    print("\nNúmero escolhido:", numero)
    print("Fatoração:", texto)
    print("Números testados na fatoração:", str(tentativasFatoracao))
    print("Números testados na listagem:", str(tentativasLista)) 
    print("Segundos gastos:", str(tempo))
