from random import randint
from multipledispatch import dispatch

class Personagem(object):
    
    nome = ""
    hpMax = 0
    mpMax = 0
    hp = 0
    mp = 0
    atk = 0
    spc = 0
    defesa = 0
    atkTemp = 0
    spcTemp = 0
    defesaTemp = 0
    status = ()    
    habilidadesAtk = ()
    habilidadesSpc = ()
    habilidadesDef = ()
#---------


def criar_Personagem(nome, hpMax, mpMax, atk, spc, defesa):
    
    personagem = Personagem()
    personagem.nome = nome
    personagem.hpMax = hpMax
    personagem.mpMax = mpMax
    personagem.hp = hpMax
    personagem.mp = mpMax
    personagem.atk = atk
    personagem.spc = spc
    personagem.defesa = defesa
    personagem.atkTemp = atk
    personagem.spcTemp = spc
    personagem.defesaTemp = defesa
    return personagem
#---------




class Habilidade:

    user = ""
    alvo = ""
    nome = ""
    texto = ""
    tipo = ""
    x = 0

    Uhp = 0
    Ump = 0
    Uatk = 0
    Uspc = 0
    Udefesa = 0 #
    Uturnos = 0

    Ahp = 0
    Amp = 0
    Aatk = 0
    Aspc = 0
    Adefesa = 0 #
    Aturnos = 0

    #Porcentagem
    atkMulti = 100
    spcMulti = 100
    AdefMulti = 100

##    def __init__(coisas basicas, tipo, lista):
##      atribuir coisas basicas
##      if tipo == "tipo":
##         outras, coisas, nao, basicas = lista
##      if tipo == "outro":
##         nao, sei, oq, la = lista
    
    @dispatch(Personagem, Personagem, str, str, str)
    def __init__(self, user, alvo, nome, tipo, texto):
        self.user = user
        self.alvo = alvo
        self.nome = nome
        self.texto = texto
        self.tipo = tipo
        
    @dispatch(Personagem, Personagem, str, str, str, int)
    def __init__(self, user, alvo, nome, tipo, texto,
                 x):
        self.user = user
        self.alvo = alvo
        self.nome = nome
        self.texto = texto
        self.tipo = tipo
        self.x = x

        
    @dispatch(Personagem, Personagem, str, str, str,
              int, int, int, int, int)
    def __init__(self, user, alvo, nome, tipo, texto,
                 Uhp, Ump, Ahp, Amp, x):
        self.user = user
        self.alvo = alvo
        self.nome = nome
        self.texto = texto
        self.tipo = tipo
        self.Uhp = Uhp
        self.Ump = Ump
        self.Ahp = Ahp
        self.Amp = Amp
        self.x = x
        
    @dispatch(Personagem, Personagem, str, str, str,
              int, int, int, int, int, int, int)
    def __init__(self, user, alvo, nome, tipo, texto,
                 Uhp, Ump, Ahp, Amp, atkMulti, spcMulti, x):
        self.user = user
        self.alvo = alvo
        self.nome = nome
        self.texto = texto
        self.tipo = tipo
        self.Uhp = Uhp
        self.Ump = Ump
        self.Ahp = Ahp
        self.Amp = Amp
        self.atkMulti = atkMulti
        self.spcMulti = spcMulti
        self.x = x

        
    @dispatch(Personagem, Personagem, str, str, str,
              int, int, int, int, int, int)
    def __init__(self, user, alvo, nome, tipo, texto,
                 Uhp, Ump, Uatk, Uspc, Udefesa, Uturnos):
        self.user = user
        self.alvo = alvo
        self.nome = nome
        self.texto = texto
        self.tipo = tipo
        self.Uhp = Uhp
        self.Ump = Ump
        self.Uatk = Uatk
        self.Uspc = Uspc
        self.Udefesa = Udefesa
        self.Uturnos = Uturnos
        
    @dispatch(Personagem, Personagem, str, str, str,
              int, int, int, int, int, int, int)
    def __init__(self, user, alvo, nome, tipo, texto,
                 Uhp, Ump, Aatk, Aspc, Adefesa, Aturnos, x):
        self.user = user
        self.alvo = alvo
        self.nome = nome
        self.texto = texto
        self.tipo = tipo
        self.Uhp = Uhp
        self.Ump = Ump
        self.Aatk = Aatk
        self.Aspc = Aspc
        self.Adefesa = Adefesa
        self.Aturnos = Aturnos
        self.x = x
        
        
    @dispatch(Personagem, Personagem, str, str, str,
              int, int, int, int, int, int,
              int, int, int, int, int, int, int)
    def __init__(self, user, alvo, nome, tipo, texto,
                 Uhp, Ump, Uatk, Uspc, Udefesa, Uturnos,
                 Ahp, Amp, Aatk, Aspc, Adefesa, Aturnos, x):
        self.user = user
        self.alvo = alvo
        self.nome = nome
        self.texto = texto
        self.tipo = tipo
        self.Uhp = Uhp
        self.Ump = Ump
        self.Uatk = Uatk
        self.Uspc = Uspc
        self.Udefesa = Udefesa
        self.Uturnos = Uturnos
        self.Ahp = Ahp
        self.Amp = Amp
        self.Aatk = Aatk
        self.Aspc = Aspc
        self.Adefesa = Adefesa
        self.Aturnos = Aturnos
        self.x = x

    def teste(self, teste):
        tipo = teste
        
        

def exec(hab):

    user = hab.user
    alvo = hab.alvo
    nome = hab.nome
    tipo = hab.tipo
    texto = hab.texto
    x = hab.x

    Uhp = hab.Uhp
    Ump = hab.Ump
    Uatk = hab.Uatk
    Uspc = hab.Uspc
    Udefesa = hab.Udefesa
    Uturnos = hab.Uturnos

    Ahp = hab.Ahp
    Amp = hab.Amp
    Aatk = hab.Aatk
    Aspc = hab.Aspc
    Adefesa = hab.Adefesa
    Aturnos = hab.Aturnos

    atkMulti = hab.atkMulti
    spcMulti = hab.spcMulti
    AdefMulti = hab.AdefMulti


    ataque = user.atkTemp * (atkMulti / 100)
    special = user.spcTemp * (spcMulti / 100)
    defesa = (100 - (alvo.defesaTemp * AdefMulti) / 100) / 100



    if "|" in texto:
        listatexto = texto.split("|")
        texto = listatexto[randint(0, len(listatexto))]

        
    #TIPOS - "ATAQUE:"
    if tipo.startswith("ataque:"):
        dano = ataque * defesa
        dano = arredondar(dano)
        dano = zero(dano)
        
        user.hp -= Uhp
        user.mp -= Ump
        
        
        alvo.hp -= dano
          

        print(user.nome, texto, alvo.nome, " e causou " + str(dano), "de dano")
        
        if tipo.endswith("lifesteal"):
            roubo = dano * (x / 100)
            roubo = arrendondar(roubo)

            user.hp += roubo
            tratar(user.hp, user.hpmax)
            print("E recuperou", roubo, "de vida")

       
        
    #TIPOS - "SPECIAL:"
    if tipo.startswith("special:"):
        dano = special * defesa
        dano = arredondar(dano)        
        dano = zero(dano)
        
        user.hp -= Uhp
        user.mp -= Ump
        
        
        alvo.hp -= dano


        print(user.nome, texto, alvo.nome, " e causou " + str(dano), "de dano")
        

    #TIPOS - "CURA:"
    if tipo.startswith("cura:"):
        user.mp -= Ump

        if tipo.endswith("simples"):
            user.hp += Uhp

        if tipo.endswith("special"):
            user.hp += special
            
        print(user.nome, "recuperou", Uhp, "de vida")




    if ("venenoso") in tipo:
        print("ADICIONAR STATUS DE VENENO")

    if ("atordoante") in tipo:
        print("ADICIONAR STATUS DE STUN")
        
    return user, alvo
        
        
            
#---------        

def arredondar(numero):
    numerofinal = numero / 10
    numerofinal = round(numerofinal) * 10
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



aliado = criar_Personagem("Aliado", 1000, 500, 50, 100, 40)
inimigo = criar_Personagem("Inimigo", 500, 200, 30, 80, 20)

a = Habilidade(aliado, inimigo, 'ataque normal', 'ataque_simples', 'atacou')
b = Habilidade(inimigo, aliado, 'ataque normal', 'ataque_simples', 'atacou')
aliado, inimigo = exec(a)


        

        

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

    

    

    





