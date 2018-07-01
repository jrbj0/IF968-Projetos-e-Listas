from random import randint

class Personagem(object):
    
    nome = ""
    hpMax = 0
    mpMax = 0
    hp = 0
    mp = 0
    ataque = 0
    special = 0
    defesa = 0
    resistencia = 0
    atkTemp = 0
    spcTemp = 0
    defTemp = 0
    resTemp = 0
    elementos = [1., 1., 1., 1., 1., 1., 1.] #Fogo, Água, Terra, Ar, Luz, Trevas
    status = [["atordoado", 0], #Perde o turno
              [["", "petrificado", "congelado", "paralisado"], 0, 0], #Respectivamente Pedra, Papel e Tesoura
              ["envenenado", 0, 0], #Dano por Valor, Longo, Removido por cura ou tempo
              ["queimando", 0, 0],  #Dano por Valor, Curto, Removido somente por tempo
              ["sangrando", 0, 0],  #Dano Porcentagem, Infinito, Removido somente por cura
              ["Ataque", 0, 0],
              ["Magia", 0, 0],
              ["Defesa", 0, 0],
              ["Resistência", 0, 0]]   
    habilidadesAtaque = [[], [], []]
    habilidadesSpecial = [[[],[]],[[],[]],[[],[]]]
    habilidadesDefesa = [[[],[],[]],[[],[],[]],[[],[],[]]]
#---------


def criar_Personagem(nome, hpMax, mpMax, ataque, special, defesa, resistencia, elementos):
    
    personagem = Personagem()
    personagem.nome = nome
    personagem.hpMax = hpMax
    personagem.mpMax = mpMax
    personagem.hp = hpMax
    personagem.mp = mpMax
    personagem.ataque = ataque
    personagem.special = special
    personagem.defesa = defesa
    personagem.resistencia = resistencia
    personagem.atkTemp = ataque
    personagem.spcTemp = special
    personagem.defTemp = defesa
    personagem.resTemp = resistencia
    personagem.elementos = elementos
    personagem.elementos.insert(0, 1.)
    
    return personagem
#---------


class Habilidade:

    user = ""
    alvo = ""
    nome = ""
    texto = ""
    tipo = ""
    lista = [0, 0, 0]

    def __init__(self, user, alvo, nome, texto, elemento, tipo, lista):
        self.user = user
        self.alvo = alvo
        self.nome = nome
        self.texto = texto
        self.elemento = elemento
        self.tipo = tipo        
        self.lista = lista    


def executar(hab):

    user = hab.user
    alvo = hab.alvo
    nome = hab.nome
    tipo = hab.tipo.upper()
    texto = hab.texto
    lista = hab.lista
    i = 0
    
    eleMulti = 1.0
    if hab.elemento:
        eleMulti = alvo.elementos[hab.elemento]
    
    if "|" in texto:
        listatexto = texto.split("|")
        texto = listatexto[randint(0, len(listatexto) - 1)]
        
    #ATAQUE
    if tipo.startswith("ATAQUE"):

        Uhp = lista[0]
        Ump = lista[1]
        atkMulti = lista[2]
        AdefMulti = lista[3]

        if eleMulti != 1:
            efetividadeElemento(alvo.nome, hab.elemento, eleMulti)

        eleMultiFisico = ((eleMulti - 1) / 2) + 1            

        atk = (user.atkTemp * atkMulti) * eleMultiFisico
        Adef = (100 - (alvo.defTemp * AdefMulti)) / 100
        
        dano = atk * Adef
        dano = arredondar(dano)
        dano = zero(dano)
        
        
        user.hp -= Uhp
        user.mp -= Ump        
        
        alvo.hp -= dano          
        
        print(user.nome, texto, alvo.nome, "e causou " + str(dano), "de dano")
        i = 4
        
    #SPECIAL
    if tipo.startswith("SPECIAL"):

        Uhp = lista[0]
        Ump = lista[1]
        spcMulti = lista[2]
        AresMulti = lista[3]
        
        if eleMulti != 1:
            efetividadeElemento(alvo.nome, hab.elemento, eleMulti)
                
        spc = (user.spcTemp * spcMulti) * eleMulti
        Ares = (100 - (alvo.resTemp * AresMulti)) / 100
        
        dano = spc * Ares
        dano = arredondar(dano)        
        dano = zero(dano)
        
        user.hp -= Uhp
        user.mp -= Ump        
        
        alvo.hp -= dano


        print(user.nome, texto, alvo.nome, "e causou " + str(dano), "de dano")
        i = 4


    #CURA
    if "CURA" in tipo:    
        
        Uhp = lista[0]
        Ump = lista[1]

        user.mp -= Ump

        cura = Uhp

        if "-MAGIC" in tipo:
            spcMulti = lista[2]
            spc = user.spcTemp * spcMulti
            spc = arredondar(spc)
            spc = zero(spc)

            cura = spc

        if "CURA:USER" in tipo:
            if user.hpMax - user.hp < cura:
                cura = user.hpMax - user.hp
            
            user.hp += cura

            print(user.nome, texto)
            print(user.nome, "recuperou", cura, "de vida")
            
        if "CURA:ALVO" in tipo:
            if alvo.hpMax - alvo.hp < cura:
                cura = alvo.hpMax - alvo.hp
            
            alvo.hp += cura

            print(alvo.nome, texto)
            print(alvo.nome, "recuperou", cura, "de vida")
        

    #LIFESTEAL
    if "LIFESTEAL" in tipo:

        lifesteal = lista[i]
        i += 1
              

        roubo = dano * lifesteal
        roubo = arredondar(roubo)

        if user.hpMax - user.hp < roubo:
            roubo = user.hpMax - user.hp

        user.hp += roubo
        tratar(user.hp, user.hpMax)
        print(user.nome, "recuperou", roubo, "de vida")
        

    #STUNS
    if "STUN" in tipo or "FREEZE" in tipo or "PETRIFY" in tipo or "PARALYZE" in tipo:
        
        turnos = lista[i]
        i += 1
        x = 1
        tipoStatus = 0        
        if "STUN" in tipo:
            x = 0            
        elif "PETRIFY" in tipo:
            tipoStatus = 1
        elif "FREEZE" in tipo:
            tipoStatus = 2
        elif "PARALYZE" in tipo:
            tipoStatus = 3

        alvo.status[x][1] = turnos
        if x:
            alvo.status[x][2] = tipoStatus
        

        plural = ""
        if turnos - 1:
            plural = "s"

        restoTexto = ""
        if x:
            ppt = ["", "Pedra", "Papel", "Tesoura"]
            restoTexto = alvo.nome + " somente pode usar " + ppt[tipoStatus] + "!"

        print(alvo.nome, "está", alvo.status[x][0][tipoStatus], "por", turnos, "turno" + plural + "!", restoTexto)
        
        
    #STATUS NEGATIVOS
    if "POISON" in tipo:
        turnos = lista[i]            
        danoturno = lista[i+1]
        i += 2
        x = 2
        if alvo.status[x][1]:
            print("O veneno em", alvo.nome, "se intensificou!")
            if alvo.status[x][1] < turnos:
                alvo.status[x][1] = turnos
            alvo.status[x][2] += danoturno
        else:
            print(alvo.nome, "está envenenado por", turnos, "turnos!")
            alvo.status[x][1] = turnos
            alvo.status[x][2] = danoturno
            
            
    if "BURN" in tipo:
        turnos = lista[i]            
        danoturno = lista[i+1]
        i += 2
        x = 3
        if alvo.status[x][1]:
            print("As chamas em", alvo.nome, "aumentaram!")
            alvo.status[x][2] += danoturno
            
        else:
            print(alvo.nome, "está em chamas por", turnos, "turnos!")
            alvo.status[x][1] = turnos
            alvo.status[x][2] = danoturno
            
              
    if "BLEED" in tipo:
        turnos = lista[i]            
        danoturno = lista[i+1]
        i += 2
        x = 4                
        if alvo.status[x][1]:
            print("O sangramento de", alvo.nome, "aumentou!")
            alvo.status[x][2] += danoturno
        else:                    
            print(alvo.nome, "está sangrando por", turnos, "turnos!")
            alvo.status[x][1] = turnos
            alvo.status[x][2] = danoturno


    #BUFFS E DEBUFFS
    if "CHANGEATK" in tipo:
        turnos = lista[i]
        modificador = lista[i + 1]
        i += 2
        atrib = 5

        if "ATK:USER" in tipo:
            user.status[atrib] = modificarAtributo(user.nome, "seu", user.status[atrib], turnos, modificador)
        if "ATK:ALVO" in tipo:
            alvo.status[atrib] = modificarAtributo(alvo.nome, "seu", alvo.status[atrib], turnos, modificador)

    if "CHANGESPC" in tipo:
        turnos = lista[i]
        modificador = lista[i + 1]
        i += 2
        atrib = 6
        
        if "SPC:USER" in tipo:
            user.status[atrib] = modificarAtributo(user.nome, "sua", user.status[atrib], turnos, modificador)
        if "SPC:ALVO" in tipo:
            alvo.status[atrib] = modificarAtributo(alvo.nome, "sua", alvo.status[atrib], turnos, modificador)

    if "CHANGEDEF" in tipo:
        turnos = lista[i]
        modificador = lista[i + 1]
        i += 2
        atrib = 7 
        if "DEF:USER" in tipo:
            user.status[atrib] = modificarAtributo(user.nome, "sua", user.status[atrib], turnos, modificador)
        if "DEF:ALVO" in tipo:
            alvo.status[atrib] = modificarAtributo(alvo.nome, "sua", alvo.status[atrib], turnos, modificador)

    if "CHANGERES" in tipo:
        turnos = lista[i]
        modificador = lista[i + 1]
        i += 2
        atrib = 8 
        if "RES:USER" in tipo:
            user.status[atrib] = modificarAtributo(user.nome, "sua", user.status[atrib], turnos, modificador)        
        if "RES:ALVO" in tipo:
            alvo.status[atrib] = modificarAtributo(alvo.nome, "sua", alvo.status[atrib], turnos, modificador)
    
        
    return user, alvo



def efetividadeElemento(alvo, elemento, multi):

    elementos = ["", "Fogo", "Água", "Terra", "Ar", "Luz", "Trevas"]
    eleNome = elementos[elemento]

    if multi > 1:
            if multi >= 2:
                print(alvo, "é altamente vulnerável a ataques do tipo", eleNome + "!")
            else:
                print(alvo, "é vulnerável a ataques do tipo", eleNome + "!")
    elif multi < 1:
        if multi <= 0:
            print(alvo, "anula ataques do tipo", eleNome + "!")
        else:
            print(alvo, "é resistente a ataques do tipo", eleNome + "!")


def modificarAtributo(alvo, seusua, status, turnos, modif):

    ao = "a"
    if seusua == "seu":
        ao = "o"

    multi = 1
    if modif >= 0:   
        parteTexto = "aumentad" + ao
    else:
        parteTexto = "diminuíd" + ao
        multi = -1

    status[1] = turnos
    status[2] = modif

    modifTexto = arredondar(modif * 100) * multi

    print(alvo, "está com", seusua, status[0], parteTexto, "em", str(modifTexto) + "% por", turnos, "turnos!")

    return status
        
        
    

    
    
        
        
            
#---------        

def arredondar(numero):
    numerofinal = round(numero) / 10
    numerofinal = numerofinal * 10
    numerofinal = int(numerofinal)
    return numerofinal
#---------

def tratar(valor, max):
    if valor > max:
        valor = max
    if valor < 0:
        valor = 0
    return valor

def zero(valor):
    if valor < 0:
        valor = 0
    return valor
    




###############################COMEÇO###############################



aliado = criar_Personagem("Aliado", 1000, 500, 50, 100, 40, 20, [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
inimigo = criar_Personagem("Inimigo", 500, 200, 30, 80, 20, 20, [20., 2, 2., .5, 0, -1.5, 1., .5])

a = Habilidade(aliado, inimigo, 'ataque normal', "ignorou", 2, 'SPECIAL: CHANGESPC:USER CHANGEDEF:ALVO CHANGERES:ALVO FREEZE', [0, 0, 1, 1, 2, 3, 0.5, 2, 0.25, 2, 0.25])
b = Habilidade(inimigo, aliado, 'ataque normal', "olhou com raiva para", 2, 'CHANGEATK CHANGEDEF CHANGESPC CHANGERES', [3, 0.5, 2, -0.5, 4, 0.1, 5, -0.2])
aliado, inimigo = executar(a)


#FAZER INTERPRETADOR DE HABILIDADES
#CHANGE[SPC](USER)[3, 0.5]

        

        

##HABILIDADES
##
##    ATAQUE
##        PEDRA
##            VENCER
##            
##        PAPEL
##            VENCER
##            
##        TESOURA
##            VENCER
##            
##    SPECIAL
##        PEDRA
##            VENCER
##            EMPATE
##            
##        PAPEL
##            VENCER
##            EMPATE
##            
##        TESOURA
##            VENCER
##            EMPATE
##            
##    DEFENDER
##        PEDRA
##            VENCER
##            EMPATE
##            PERDER
##            
##        PAPEL
##            VENCER
##            EMPATE
##            PERDER
##            
##        TESOURA
##            VENCER
##            EMPATE
##            PERDER

    

    

    





