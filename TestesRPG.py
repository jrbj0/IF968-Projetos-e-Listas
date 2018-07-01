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
    elementos = {"": 1., "fogo": 1., "agua": 1., "terra": 1., "ar":1., "luz":1., "trevas":1.} #Fogo, Água, Terra, Ar, Luz, Trevas
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
    def __init__(self, nome, texto, elemento, lista):
        self.nome = nome
        self.texto = texto
        self.elemento = elemento
        self.lista = lista
        

def executarHabilidade(hab, user, alvo):
    
    nome = hab.nome
    texto = hab.texto
    lista = hab.lista
        
    #REPLACES DO TEXTO
    texto = texto.replace("(USER)", user.nome)
    texto = texto.replace("(ALVO)", alvo.nome)
    if "|" in texto:
        texto = texto.split("|")
        texto = texto[randint(0, len(texto) - 1)]
    
    #TEXTO DOS ELEMENTOS
    eleMulti = 1.0
    textoElementos = ""
    if hab.elemento:
        eleMulti = alvo.elementos[hab.elemento]
        textoElementos = efetividadeElemento(alvo.nome, hab.elemento, eleMulti)

    textos = [user.nome + " usou " + nome, texto, textoElementos]
    for i in range(len(lista)):
        #CONVERTER EM FLOAT
        valores = []
        tipo = lista[i].split("|")        
        tipo[-1] = tipo[-1].split(",")
        for x in range(len(tipo[-1])):
            valores.append(float(tipo[-1][x]))
        tipo.pop()

        #ALVO DA HABILIDADE
        alvoEfeito = alvo
        if ":" in tipo[0]:
            tipo[0] = tipo[0].split(":")
            if tipo[0][-1].upper() == "USER":
                alvoEfeito = user
            tipo[0] = tipo[0][0]

        textos, user, alvoEfeito = calcularHabilidade(textos, user, alvoEfeito, tipo, valores, eleMulti)

    for i in range(len(textos)):
        print(textos[i])

    return user, alvo
        

def calcularHabilidade(textos, user, alvo, tipo, valores, eleMulti):

    dano = 0
    
    #ATAQUE
    if tipo[0].startswith("ATAQUE"):

        atkMulti = valores[0]
        AdefMulti = valores[1]      

        atk = (user.atkTemp * atkMulti) * eleMulti
        Adef = (100 - (alvo.defTemp * AdefMulti)) / 100
        
        dano = atk * Adef
        dano = arredondar(dano)
        dano = zero(dano)
        if alvo.hp < dano:
            dano = alvo.hp
            
        dano = zero(dano)
        alvo.hp -= dano          
        
        textos.append(user.nome + " causou " + strx(dano) + " de dano em " + alvo.nome)
        
    #SPECIAL
    if tipo[0].startswith("SPECIAL"):

        spcMulti = valores[0]
        AresMulti = valores[1]
                
        spc = (user.spcTemp * spcMulti) * eleMulti
        Ares = (100 - (alvo.resTemp * AresMulti)) / 100
        
        dano = spc * Ares
        dano = arredondar(dano)        
        dano = zero(dano)        
        if alvo.hp < dano:
            dano = alvo.hp
            
        dano = zero(dano)
        alvo.hp -= dano

        textos.append(user.nome + " causou " + strx(dano) + " de dano em " + alvo.nome)

    #LIFESTEAL
    if "-LIFESTEAL" in tipo:

        lifesteal = valores[2]
        roubo = dano * lifesteal
        roubo = arredondar(roubo)
        if user.hpMax - user.hp < roubo:
            roubo = user.hpMax - user.hp
        
        user.hp += roubo
        print(user.nome, "recuperou", roubo, "de vida")
        

    #VIDA
    if tipo[0].startswith("VIDA"):

        vida = valores[0]
        atrib = ""
        tipos = [tipo[0]]
        if ":" in tipo:
            atrib = tipo.split("/")[-1]
        
        if atrib == "SPC":
            spcMulti = valores[0]
            spc = user.spcTemp * spcMulti
            spc = arredondar(spc)
            spc = zero(spc)
            vida = spc
        
        negativoMulti = 1
        if vida >= 0:
            parteTexto = "recuperou"                
            if alvo.hpMax - alvo.hp < vida:
                vida = alvo.hpMax - alvo.hp
        else:
            if user.nome == alvo.nome and user.hp == alvo.hp:
                parteTexto = "gastou"
            else:
                parteTexto = "perdeu"
            negativoMulti = -1
            if alvo.hp < vida:
                vida = alvo.hp
            
        alvo.hp += vida
        vida = vida * negativoMulti

        if "*" in tipo[0]:
            textos.append(alvo.nome + " " + parteTexto + " " + strx(vida) + " de vida!")

    #MANA
    if tipo[0].startswith("MANA"):

        mana = valores[0]
        atrib = ""
        tipos = [tipo[0]]
        if ":" in tipo:
            atrib = tipo.split("/")[-1]
        
        if atrib == "SPC":
            spcMulti = valores[0]
            spc = user.spcTemp * spcMulti
            spc = arredondar(spc)
            spc = zero(spc)
            mana = spc
        
        negativoMulti = 1
        if mana >= 0:
            parteTexto = "recuperou"                
            if alvo.mpMax - alvo.mp < mana:
                mana = alvo.mpMax - alvo.mp
        else:
            if user.nome == alvo.nome and user.mp == alvo.mp:
                parteTexto = "gastou"
            else:
                parteTexto = "perdeu"
            negativoMulti = -1
            if alvo.mp < mana:
                mana = alvo.mp
            
        alvo.mp += mana
        mana = mana * negativoMulti

        if "*" in tipo[0]:
            textos.append(alvo.nome + " " + parteTexto + " " + strx(mana) + " de mana!")        

    #STUNS
    if tipo[0].startswith("STUN") or tipo[0].startswith("FREEZE") or tipo[0].startswith("PETRIFY") or tipo[0].startswith("PARALYZE"):
        turnos = valores[0]
        x = 1
        tipoStatus = 0        
        if tipo[0].startswith("STUN"):
            x = 0            
        elif tipo[0].startswith("PETRIFY"):
            tipoStatus = 1
        elif tipo[0].startswith("FREEZE"):
            tipoStatus = 2
        elif tipo[0].startswith("PARALYZE"):
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

        textos.append(alvo.nome + " está " + alvo.status[x][0][tipoStatus] + " por " + strx(turnos) + " turno" + plural + "! " + restoTexto)
        
        
    #STATUS NEGATIVOS
    if tipo[0].startswith("POISON") or tipo[0].startswith("BURN") or tipo[0].startswith("BLEED"):
        turnos = valores[0]         
        danoturno = valores[1]
                
        if tipo[0].startswith("POISON"):
            x = 2
            if alvo.status[x][1]:
                textos.append("O veneno em " + alvo.nome + " se intensificou!")
                if alvo.status[x][1] < turnos:
                    alvo.status[x][1] = turnos
                alvo.status[x][2] += danoturno
            else:
                textos.append(alvo.nome + " está envenenado por " + strx(turnos) + " turnos!")
                alvo.status[x][1] = turnos
                alvo.status[x][2] = danoturno
                
                
        if tipo[0].startswith("BURN"):
            x = 3
            if alvo.status[x][1]:
                textos.append("As chamas em " + alvo.nome + " aumentaram!")
                alvo.status[x][2] += danoturno
                                
            else:
                textos.append(alvo.nome + " está em chamas por " + strx(turnos) + " turnos!")
                alvo.status[x][1] = turnos
                alvo.status[x][2] = danoturno
                
                  
        if tipo[0].startswith("BLEED"):
            x = 4                
            if alvo.status[x][1]:
                textos.append("O sangramento de " + alvo.nome + " aumentou!")
                alvo.status[x][2] += danoturno
            else:                    
                textos.append(alvo.nome + " está sangrando por " + strx(turnos) + " turnos!")
                alvo.status[x][1] = turnos
                alvo.status[x][2] = danoturno
                

    #BUFFS E DEBUFFS
    if tipo[0].startswith("CHANGE"):
        atributo = tipo[0].split("/")[-1]
        turnos = valores[0]
        modificador = valores[1]

        seusua = " sua "
        atrib = 0
        if atributo == "ATK":
            atrib = 5
            seusua = " seu "            
        elif atributo == "SPC":
            atrib = 6            
        elif atributo == "DEF":
            atrib = 7
        elif atributo == "RES":
            atrib = 8

        if atrib:
            alvo.status[atrib], textoStatus = modificarAtributo(alvo.nome, seusua, alvo.status[atrib], turnos, modificador)
            textos.append(textoStatus)
        
    return textos, user, alvo



def efetividadeElemento(alvo, elemento, multi):

    elementos = ["", "Fogo", "Água", "Terra", "Ar", "Luz", "Trevas"]
    eleNome = elementos[elemento]
    texto = ""
    if multi > 1:
            if multi >= 2:
                texto = alvo + " é altamente vulnerável a ataques do tipo " + eleNome + "!"
            else:
                texto = alvo + " é vulnerável a ataques do tipo " + eleNome + "!"
    elif multi < 1:
        if multi <= 0:
            texto = alvo + " anula ataques do tipo " + eleNome + "!"
        else:
            texto = alvo + " é resistente a ataques do tipo " + eleNome + "!"

    return texto


def modificarAtributo(alvo, seusua, status, turnos, modif):

    ao = "a"
    if seusua == "seu":
        ao = "o"
    multi = 1
    if modif >= 0:   
        parteTexto = " aumentad" + ao
    else:
        parteTexto = " diminuíd" + ao
        multi = -1

    status[1] = turnos
    status[2] = modif
    modifTexto = arredondar(modif * 100) * multi
    textoStatus = (alvo + " está com" + seusua + status[0] + parteTexto + " em " + strx(modifTexto) + "% por " + strx(turnos) + " turnos!")

    return status, textoStatus
    
    
        
        
            
#---------        

def arredondar(numero):
    numerofinal = round(numero) / 10
    numerofinal = numerofinal * 10
    numerofinal = int(numerofinal)
    return numerofinal

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

def strx(valor):
    return str(int(valor))    




###############################COMEÇO###############################



aliado = criar_Personagem("Aliado", 1000, 500, 50, 100, 40, 20, [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
inimigo = criar_Personagem("Inimigo", 500, 200, 30, 80, 20, 20, [20., 2, 2., .5, 0, -1.5, 1., .5])

c = Habilidade("Olhar Gélido", "(USER) ignorou (ALVO)|(USER) olhou com raiva para (ALVO)", 2,
               ["SPECIAL|1, 1", "VIDA*:USER|-50", "MANA:USER|-10", "FREEZE|2", "BLEED|2, 5", "CHANGE/SPC:USER|3, 0.5", "CHANGE/RES:ALVO|2, -0.25"])

aliado, inimigo = executarHabilidade(c, aliado, inimigo)

#a = Habilidade(aliado, inimigo, 'ataque normal', "ignorou", 2, 'SPECIAL: CHANGESPC:USER CHANGEDEF:ALVO CHANGERES:ALVO FREEZE', [0, 0, 1, 1, 2, 3, 0.5, 2, 0.25, 2, 0.25])
#b = Habilidade(inimigo, aliado, 'ataque normal', "olhou com raiva para", 2, 'CHANGEATK CHANGEDEF CHANGESPC CHANGERES', [3, 0.5, 2, -0.5, 4, 0.1, 5, -0.2])
#aliado, inimigo = executar(a)


      

        

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
               
