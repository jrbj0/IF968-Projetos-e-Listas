texto = input()

while texto == "" or texto == " " * len(texto):
    print("Favor inserir um texto que não esteja em branco!")
    texto = input()

lista = []
palavra = ""
for i in range(0, len(texto)):

    c = texto[i]
    if c != " " and c != "," and c != "." and c != "?" and c != "!":
        palavra = palavra + c
    else:
        if palavra:
            lista.append(palavra)
            palavra = ""

if palavra:
    lista.append(palavra)

print(lista)
