class Personagem(object):
    
    nome = ""
    hpMax = 0
    hp = 0
    mpMax = 0
    mp = 0
    atk = 0
    atkTemp = 0
    spc = 0
    spcTemp = 0
    defesa = 0
    defesaTemp = 0
    tempTurnos = 0
    stun = False
    habilidadesAtk = ()
    habilidadesSpc = ()
    habilidadesDef = ()
#---------


def criar_Personagem(nome, hpMax, mpMax, atk, spc, defesa):
    
    personagem = Personagem()
    personagem.nome = nome
    personagem.hpMax = hpMax
    personagem.hp = hpMax
    personagem.mpMax = mpMax
    personagem.mp = mpMax
    personagem.atk = atk
    personagem.atkTemp = atk
    personagem.spc = spc
    personagem.spcTemp = spc
    personagem.defesa = defesa
    personagem.defesaTemp = defesa
    return personagem
#---------


def escolher_Classe(classeEscolhida):
    
    switcher = {
        
        "G":    criar_Personagem(nome,
                "Guerreiro",                          #Classe
                400,                                  #HP
                50,                                   #MP
                40,                                   #Ataque
                100,                                  #Special
                20),                                  #Defesa
        
        "A":    criar_Personagem(nome,
                "Arqueiro",                           #Classe
                300,                                  #HP
                500,                                  #MP
                30,                                   #Ataque
                150,                                  #Special
                10),                                  #Defesa
        
        "M":    criar_Personagem(nome,
                "Mago",                               #Classe
                250,                                  #HP
                500,                                  #MP
                15,                                   #Ataque
                100,                                  #Special
                10),                                  #Defesa

    }
    return switcher.get(classeEscolhida, "")
#---------


def escolher_Status():
    classe = input("Insira o nome da classe:\n")

    if classe.upper() == "LAVAR CACHORROS":
        status = criar_Personagem("WASH DOGES", "HAQUE",
                                  5000, 5000, 100, 500, 100, )
    else:
        status = criar_Personagem(nome,
                                  classe,
                                  int(input("HP:\t\t")),                                 
                                  int(input("MP:\t\t")),                                   
                                  int(input("Ataque:\t\t")),                                   
                                  int(input("Special:\t")),                                 
                                  int(input("Defesa:\t\t")),                                  
                                  int(input("Destreza:\t\t")),                                   
                                  input("Insira o texto do Ataque:\n"),               
                                  input("Insira o texto do Special:\n"))

    return status
#---------

def preparar_Inimigos():
    
    iNome = ['Slime', 'Rato Gigante', 'Lobo', 'Morcego', 'Ladrão',
            'Bárbaro', 'Zumbi', 'Esqueleto', 'Kobold', 'Gnoll',
            'Orc', 'Bruxo', 'Urso', 'Vampiro', 'Lobisomem',
            'Ogro', 'Basilisco', 'Minotauro', 'Manticore', 'Cérbero']

    iHP = [400, 350, 500, 350, 600,
           800, 600, 600, 500, 600,
           1200, 600, 1000, 1000, 1000,
           1500, 1800, 1400, 1400, 1500]

    iChanceSpecial = [10,  15, 15, 15, 15,
                      5, 10, 10, 15, 20,
                      15, 35, 20, 25, 25,
                      10, 25, 15, 25, 25]                      

    iAtaque = [50, 70, 90, 60, 100,
               150, 80, 80, 120, 130,
               200, 100, 160, 200, 350,
               300, 400, 320, 350, 350]

    iSpecial = [80, 80, 100, 80, 120,
                170, 120, 100, 150, 150,
                280, 500, 200, 300, 400,
                500, 600, 500, 600, 600] 

    iDefesa = [30, 20, 20, 10, 40,
               40, 20, 40, 20, 30,
               60, 20, 40, 50, 50,
               70, 100, 80, 60, 60]

    iTexto = ['tentou derrubar', 'arranhou', 'cortou', 'mordeu', 'tentou esfaquear',
              'cortou com o montante', 'tentou morder', 'golpeou', 'cortou com sua faca', 'atacou com sua lança',
              'golpeou com o machado', 'lançou um raio em', 'deu uma patada em', 'cortou', 'mordeu',
              'golpeou com um tronco', 'tentou morder', 'golpeou com seu martelo', 'tentou estraçalhar', 'tentou rasgar']

    iTextoSpecial = ['derreteu um pouco do braço de', 'mordeu a perna de', 'mordeu a barriga de', 'mordeu o pescoço de', 'cortou o ombro de',
                     'golpeou a cabeça de', 'mordeu o braço de', 'acertou o estômago de', 'esfaqueou as costas de', 'perfurou a mão de',
                     'cortou o antebraço de', 'acertou uma lança de gelo em', 'mordeu o ombro de', 'drenou o sangue de', 'arranhou o tórax de',
                     'esmagou', 'cuspiu uma nuvem de fogo em', 'perfurou com o chifre o peito de', 'cuspiu um jato de veneno em', 'lançou vários jatos de fogo em']

    listaInimigos = []

    for i in range(0, dificuldade * 5):

        inimigo = criar_Personagem(iNome[i], "", iHP[i], iChanceSpecial[i],
                                   iAtaque[i], 0, iDefesa[i])
        
        listaInimigos.append(inimigo)

    return listaInimigos
#---------


from multipledispatch import dispatch

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
    Udefesa = 0         #Porcentagem
    Uturnos = 0

    Ahp = 0
    Amp = 0
    Aatk = 0
    Aspc = 0
    Adefesa = 0         #Porcentagem
    Aturnos = 0

    #Porcentagem
    atkMulti = 100
    spcMulti = 100
    AdefMulti = 100
    
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
    defesa = (100 - (alvo.defesaTemp * AdefMulti) / 100) / 100
    
    if tipo == "ataque_simples":
        dano = ataque * defesa
        print(ataque)
        print(defesa)
        dano = arredondar(dano)
        user.hp -= Uhp
        user.mp -= Ump

        if dano < 0:
            dano = 0
        
        alvo.hp -= dano

        print(user.nome, texto, alvo.nome, " e causou " + str(dano), "de dano")

    if tipo == "special_simples":
        dano = ataque * defesa
        print(ataque)
        print(defesa)
        dano = arredondar(dano)
        user.hp -= Uhp
        user.mp -= Ump

        if dano < 0:
            dano = 0
        
        alvo.hp -= dano

        print(user.nome, texto, alvo.nome, " e causou " + str(dano), "de dano")
        

    if tipo == "cura_simples":
        cura = Uhp

        
    return user, alvo
        
        
            
#---------        

def arredondar(numero):
    numerofinal = numero / 10
    numerofinal = round(numerofinal) * 10
    return numerofinal
#---------       
               


def multiplicador_Aliado(level):
    multi = round(((level * 2) ** 2))
    multi = multi / 10
    multi = (multi + 10) / 10
    return round(multi, 1)

def multiplicador_Inimigos(level, dificuldade):
    multi = round(level * (1.5 + (dificuldade/2)))
    multi = (multi ** 2) / 10
    multi = ((multi + 2) / 20) + (dificuldade)/10
    return round(multi, 1)

def testar_Multiplicadores():
    for x in range(1, 20):
        print("Aliado LVL" + str(x) + ": " + str(multiplicador_Aliado(x)) + "\t" +
          "Inimigo LVL" + str(x) + ": " + str(multiplicador_Inimigos(x, 2)))
#---------
    




###############################COMEÇO###############################




print("Bem vindo a RPGZin")
print("RPGZin é um vasto mundo cheio de aventuras...")
print("Infelizmente você está preso em um ciclo infinito de batalhas! :)")
print("\nAgora que você já conhece o mundo e sabe que não vai poder explorá-lo...")

nome = ""
while not nome:
    nome = input("Quem é você?\n")
    
print("\nCerto,", nome, ", resta saber qual é sua classe...")

while True:
    classe = input("(G)uerreiro, (A)rqueiro ou (M)ago?\n").upper()
    
    if classe == "C":
        heroi = escolher_Status()
    else:        
        heroi = escolher_Classe(classe)

    print("")
    
    if(heroi != ""):
        print("OK,", heroi.nome + ", seus Status são:")
        print("Classe:\t\t\t\t" + heroi.classe,
              "\nHP:\t\t\t\t" + str(heroi.hp),
              "\nMP:\t\t\t\t"+str(heroi.mp),
              "\nAtaque:\t\t\t\t" + str(heroi.atk),
              "\nEspecial:\t\t\t"+str(heroi.spc),
              "\nDefesa:\t\t\t\t" + str(heroi.defesa))
        print("\nEstá tudo certo?")
        if input("(S)im ou (N)ão?\n").upper() == "S":
            break

    print("")


print("\n\nMuito bem, agora que você já está preparado...")
print("Qual a dificuldade que você pretende enfrentar?")

while True:
    dificuldade = input("(1) Fácil\n(2) Normal\n(3) Difícil\n")
    
    if dificuldade < "a":
        dificuldade = int(dificuldade)
        if dificuldade < 4 and dificuldade > 0:
            break
        elif dificuldade == 4:
            print("*MODO EXPERT ATIVADO*")
            break

listaInimigos = preparar_Inimigos()



        

        
        

    

    

    





