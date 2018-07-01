#RPG DO FELIPINHO

continuar = True
batalhas = []
while continuar:
    string = input("[HP1] [HP2] [ATK] [DANO)\nMaximo de 10 para cada\n")
    string = string.split(" ")

    status = []
    for i in range(len(string)):
        if string[i] and len(status) < 4:
            status.insert(i, int(string[i]))

    if len(status) == 4:
        #Energia Vital
        EV1 = (status[0])
        EV2 = (status[1])
        #Força de Ataque
        AT = (status[2])
        #Capacidade de Dano
        D = status[3]
    else:
        print("Inválido!\n")
        status = [0, 0, 0, 0]

    if status == [0, 0, 0, 0]:
        continuar = False
    else:
        ok = True
        if (EV1 < 1 or EV2 > 10) or (EV2 < 1 or EV2 > 10):
            ok = False
        elif AT < 1 or AT > 5:
            ok = False
        elif D < 1 or D > 10:
            ok = False
        if ok:
            batalhas.append(status)
            break
            


vitorias = []

from random import randint
for i in range(len(batalhas)):
    venceu = 0
    for x in range(0, 1000000):
        EV1 = batalhas[i][0]
        EV2 = batalhas[i][1]
        AT = batalhas[i][2]
        D = batalhas[i][3]
        while EV1 > 0 and EV2 > 0:
            dado = randint(1, 6)
            if dado <= AT:
                EV2 -= D
                EV1 += D
            else:        
                EV1 -= D
                EV2 += D

        if EV1 > 0:
            venceu += 1

    vitorias.append(round(venceu / 10000, 1))

for i in range(len(vitorias)):
    print("1 venceu " + str(vitorias[i]) + "% das vezes")
    
    
    
    


    



