#conjunto1 = [1, 2, 3, 6, 4, 5]
#conjunto2 = [1, 2, 3, 4, 5]
conjunto1 = [12, 13, 14, 15, 18, 50, 19]
conjunto2 = list(range(0, 50))

subtracao = []
for i in range(0, len(conjunto1)):

    unico = True
    for x in range(0, len(conjunto2)):
        if conjunto1[i] == conjunto2[x]:
            unico = False

    if unico:
        subtracao.append(conjunto1[i])

uniao = subtracao + conjunto2

print(uniao)
print(subtracao)
