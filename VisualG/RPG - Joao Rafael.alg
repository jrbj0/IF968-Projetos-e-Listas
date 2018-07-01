algoritmo "RPG"
//Feito por: João Rafael
//Infelizmente não foi por fins lucrativos...
//...até hoje to esperando a Steam pedir pra eu colocar esse jogo lá e eu ficar rico ;-;


var
HPH, HPI, STRH, STRI, DEFH, DEFI, MP, MAG: numerico            //Status
Dano, DEFLuta, AcInim, DanoInim, Critico: numerico                     //Valores para a luta
Nome, Inimigo, Classe, masoq, preparado, tantofaz, Acao, Arma, Habilidade: caracter                             //H = Herói I = Inimigo
invalido, invalido2, hack, luta, MPSuficiente: logico                                                          // STR = Força DEF = Defesa HP = Pontos de Vida
inicio


      //Bem-vindo ao tutorial de... 'COMO SER DOIDO IGUAL AO JOÃO'
     //Boa sorte!



masoq<-"n"                           //Atribuindo valores inicias para o MP e o "masoq" ("masoq" vem de masoquista, porque você escolheu o dragão negro da morte morrida!)
MPsuficiente<-Verdadeiro             //De acordo com Cloves, isso se chama iniciar uma variavel

escreval ("Qual o nome do Héroi?")
         Leia (Nome)
repita                                      //Na minha cabeça as escolhas funcionam melhor assim, eu sei que não vimos isso na aula ainda... mas eu pesquisei '-'
      escreval ("Qual a classe de " ,nome, "?")
      escreval (" Guerreiro (W), Arqueiro (A), Mago (M)")
               Leia (Classe)
               escolha (Classe)

                       caso "W"                              //preste atenção que o W está entre " "
                            HPH<-200                             //Para a luta funcionar, eu usei o HPH, STRH etc para ser um valor fixo pra cada classe
                            STRH<-20
                            DEFH<-10
                            Classe<-"Guerreiro"    //atribui a variavel 'classe' para "Guerreiro"
                            Invalido<-Falso    //invalido para fexar o repita
                            MAG<-30         //isso é o dano da habilidade
                            MP<-5
                            Arma<-"cortou com a sua Espada o "                //Essas são as falas pra não ficar igual pra todos
                                                                              //Porque um guerreiro não acerta flechas nos outros
                                                                              //Isso é mais por uma questão estética, se não estiver entendendo, não precisa usar
                            Habilidade<-"Sua espada começa a flamejar e você rapidamente desfere um golpe!"

                       caso "A"
                            HPH<-150
                            STRH<-25
                            DEFH<-5
                            Classe<-"Arqueiro"
                            MP<-10
                            MAG<-35
                            Invalido<-Falso
                            Arma<-"acertou uma flecha no"
                            Habilidade<-"Você se concentra... e acerta exatamente no coração do inimigo!"

                       caso "M"
                            HPH<-100
                            STRH<-15
                            DEFH<-2
                            Classe<-"Mago"
                            MAG<-50
                            MP<-50             //note que os MPs e as MAGs são diferentes também, porque a magia de um mago é diferente da do guerreiro por exemplo
                            Invalido<-Falso
                            Arma<-"bateu com seu cajado no"
                            Habilidade<-"Você lança uma rajada de bolas de fogo diretamente no inimigo!!"

                       outrocaso
                                escreval ("Inválido")     //caso a pessoa escreva algo que n seja W, A ou M ele deixa a variavel invalido como verdadeiro
                                Invalido<-Verdadeiro        //para o ATE ali embaixo funcionar
                                
               fimescolha
ate invalido=falso
fimrepita


Escreval ("Como você escolheu " ,classe)
escreval ("Você tem" ,HPH, " de Pontos de Vida (HP)," ,MP, " de MP " ,STRH, " de força e" ,DEFH, " de defesa")
escreval (" ")                          //você pode colocar as variaveis dentro do escreval e junto com as falas
         //^ pra pular uma linha
repita
      Escreval ("Quem é o seu inimigo?")
         timer 200                                    //Também não aprendemos 'timer" mas é bem fácil '-'
      Escreva ("Slime (S), Bandido (B)... ou")
         timer 100
         escreva (".")
         timer 100
         escreva (".")      //só pra fazer o efeito das ...
         timer 100
         escreva (".")
         timer 500
      escreval (" ")
      escreval ("Dragão Negro da Morte Morrida (DN)") //Só uma ideia retardada para fins humorísticos
      Leia (Inimigo)

      escolha (Inimigo)

               caso "S"
                  Inimigo<-"Slime"               //mesma coisa dali de cima
                  HPI<-75
                  STRI<-10
                  DEFI<-5
                  Invalido2<-Falso       //eu acho que eu podia usar a mesma variavel "invalido"... mas não percebi na hora

               caso "B"
                  Inimigo<-"Bandido"
                  HPI<-120
                  STRI<-20
                  DEFI<-10
                  Invalido2<-Falso
                  
               caso "DN"
                  Inimigo<-"Dragão Negro da Morte Morrida"
                  HPI<-8001 //O HP DELE É DE MAIS DE 8000!! *Quebra Google Glass Sayajin*
                  STRI<-45
                  DEFI<-20
                                Escreval ("Errr... você tem certeza disso? O.o'")
                                Escreval ("Sim = Y    Não = N")
                                Leia (masoq)
                                       escolha (masoq)
                                               caso "Y"                                  //Caso você escolher o Dragão...
                                                    hack<-Verdadeiro                     //eu fiz algo meio cômico e inútil
                                                    Invalido2<-Falso                     //mas foi legal e aprendi algumas coisas

                                       
                                               caso "N"
                                                    Invalido2<-Verdadeiro

                                               outrocaso
                                                    escreval ("Vou levar isso como um 'não'")
                                                    Invalido2<-Verdadeiro
                                      fimescolha

               outrocaso
                  Invalido2<-Verdadeiro


      fimescolha

ate invalido2=falso
fimrepita

timer 1000            //limpa a tela porque nesse momento tem muita coisa
limpatela





repita
timer 500

      escreval ("Você, nobre " ,classe, " " ,nome, " está preparado para lutar...")
      escreval ("contra o " ,inimigo, "?")    //preste atenção em como as variaveis estão escritas e nos espaços que eu dei entre elas
      escreval ("Sim (Y)     Não (N)")
      Leia (preparado)
                      escolha (preparado)
                              caso "Y"
                              luta<-verdadeiro
                              
                              caso "N"
                              luta<-falso         //usando o mesmo conceito do "invalido" só que ficou meio que ao contrário
                              escreva (.)
                              timer 200
                              escreva (.)
                              timer 200
                              escreva (.)
                              timer 1500
                              escreval ("... e agora?")
                              
                              outrocaso
                              luta=falso
                              
                      fimescolha
ate luta=verdadeiro
fimrepita
                              
se masoq="Y" entao   //masoq seria se você escolheu o dragão
escreval ("Tem certeza?")
         Leia (tantofaz)

              se tantofaz="y" entao
                 escreval ("Adeus...")
              fimse
                                           //foi só uma brincadeira '-'
              se tantofaz="n" entao
                 escreval ("MESMO ASSIM VOCÊ VAI!")
              fimse
fimse

timer 500
limpatela


escreval ("Imagine uma musiquinha de fundo")
         timer 500                                     //outra brincadeira besta
escreval ("*Musiquinha clichê de batalha de RPGs*")    //eu tava fazendo esse codigo por 6 horas seguidas
         timer 500                                     //se não fosse essas besteiras que eu coloquei
                                                       //eu ficaria muito entediado pra continuar

//Fim da preparação da luta (3 horas e meia... parece dragon ball ;-;)


repita
  DanoInim<-0
  Dano<-0              //Vou explicar mais a frente, no final de cada turno as variaveis resetam
  DEFLuta<-DEFH        //se não, quando você colocasse pra defender, a sua defesa iria ser *3 e ficaria pra sempre
                       //ai no outro turno você continuaria com def*3 e não faria sentido
  limpatela
  Escreval (nome, " tem " ,HPH, " de HP e " ,mp, " de MP restantes.")    //Cada começo de turno ele mostra quanto de HP cada um tem
  Escreval (inimigo, " tem " ,HPI, " de HP restante.")                    //isso é importante
  timer 1000
  Escreval (" ")
  Escreval ("O que você vai fazer?")
  Escreval ("Atacar (A) ou Defender (D) ou Usar uma Magia (M)")
  Escreval ("Cada vez que você escrever errado você perde a vez!") //Facilitar testes, diminuir o codigo e preguiça
         Leia (acao)                //A D ou M
         timer 500

                 escolha (acao)
              
                      Caso "A"
                           escreval ("Você " ,arma ,inimigo)  //lembra do "arma" la em cima? muda de acordo com a classe que você escolhe
                           Dano<-(STRH-DEFI)+randi(10)            //esse randi é pra a luta não ser exatamente igual sempre
                           Critico<-randi(101)
                                                                  se classe= "Arqueiro" entao
                                                                  critico<-critico+15             //O Arqueiro tem mais chance de critico :D
                                                                  fimse
                                                                       se critico>80 entao
                                                                       escreval ("UM ATAQUE CRÍTICO!")        //Não tinha isso antes, mas eu coloquei... ficou legal '-'
                                                                       Dano<-Dano*2                           //tava pensando em colocar evasivas também...
                                                                       fimse

                           escreval ("Você causou " ,dano, " de dano no " ,inimigo)                 //coloquei um número aleatório (que a gente também não viu) pra ficar melhor
                           HPI<-HPI-Dano            //a variavel dano calcula e mostra o dano que você causou


                      Caso "D"
                           escreval ("Você está defendendo! (DEF*3)")
                           DefLuta<-DEFH*3+randi(15)   //se você defender sua defesa vai multiplicar por 3 e mais um numero aleatorio até 5
                            //o defluta é que nem eu expliquei la em cima
                            //se não tivesse ele, as mudanças na DEFH seriam permanentes e não faria sentido
                           
                      Caso "M"
                              se MP<=0 entao             //se não tiver isso, depois que acabar o MP ele iria ficar com -5 -10 -15 etc
                                 Escreval ("Você não tem MP suficiente!!")
                                 Escreval (nome, " perdeu o turno!")
                                 MPSuficiente<-Falso
                              fimse

                           se MPSuficiente=Verdadeiro entao     //Porém se você tiver MP suficiente...
                              escreval (Habilidade)             // a Habilidade funciona que nem o "arma" lá em cima
                              Dano<-(MAG-DEFI)+randi(30)         //numero aleatorio pra deixar mais interessante
                              escreval ("Você causou " ,dano, "de dano com sua habilidade no " ,inimigo)
                              HPI<-HPI-Dano
                              MP<-MP-5  //diminui o MP
                           FimSe

                           
                      outrocaso
                           escreval ("Inválido, escolha entre (A), (D) e (M)")
                           escreval ("Você não fez nada!")       //Se nao digitar a d ou m ele pula a vez

                 fimescolha

  timer 1000
  Escreval ("É a vez do " ,inimigo)
  timer 500                              //Descobri que o Randi não gera o numero entre ( )... tipo, ele vai gerar de 1 até 3
                                            //Se fosse Randi (5) ele só geraria 1 até 4
      AcInim<-Randi(4)                //essa foi a parte que eu achei mais bem bolada... até agora não sei como pensei nisso O.o
                Se AcInim<3 entao          //ele gera um numero aleatorio até 3 pro AcInim (ação do inimigo)
                   Escreval ("O " ,inimigo, " vai atacar!")           //se for menor que 3 ele ataca normal    (1 a 2, ou seja, 66% de chance)
                   DanoInim<-(STRI+Randi(5))-DEFLuta            //randi 5 pra deixar mais legal... de novo
                   Escreval (inimigo, " causou " ,DanoInim, " de dano em " ,nome)
                   HPH<-HPH-DanoInim
                   timer 500

                Fimse

                Se AcInim=3 entao          //Se der 3, o inimigo dá um ataque mais forte, que seria a magia dele
                   Escreval (inimigo, " vai usar uma magia!!")   //fiz isso porque se não o inimigo só ia ficar atacando normal e iria ser muito chato
                   DanoInim<-(STRI*randi(4))-DefLuta     //pode dar muito dano... ou um dano normal, depende da sorte
                   Escreval (nome, " recebeu " ,danoinim, " de dano!")    //achei isso bem legal '-'
                   HPH<-HPH-DanoInim
                Fimse
                
                Se Hack=verdadeiro entao                            //No fim do primeiro turno, se você estiver lutando contra o dragão
                   Escreval ("DE REPENTE UM METEORO CAI NA CABEÇA DO DRAGÃO!!!")   //eu coloquei essa variavel pra ele perder 7950 de life dele... ele tinha mais de 8000
                   Escreval ("Rápido! Essa é sua chance")
                   HPI<-HPI-7950
                   Hack<-falso          //pra não repetir isso de novo no outro turno
                fimse
                           //Quando um dos personagens ficar com 0 ou menos de HP, a luta acaba
ate (HPH<=0)ou (HPI<=0)  //Sem o " <= " o personagem ficava com -20 de life ou algo do tipo
fimrepita

se HPH<=0 entao
         Escreval (nome, " foi derrotado por " ,inimigo, "!!!")       //é... você perdeu '-'
         timer 500
         Limpatela
         timer 200
         Escreva ("G")
         timer 200
         Escreva ("A")
         timer 200
         Escreva ("M")
         timer 200
         Escreva ("E")
         timer 200
         Escreva (" ")
         timer 200                     //frescura pra fazer o GAME OVER aparecer devagar :x
         Escreva ("O")
         timer 200
         Escreva ("V")
         timer 200
         Escreva ("E")
         timer 200
         Escreva ("R")
         timer 200
         Escreva ("!")
         timer 1500

fimse

se HPI<=0 entao
         Escreval (inimigo, " foi derrotado por " ,nome, "!")
         timer 500                                                  //PARABENS! VOCÊ GANHOU UM JOGO QUE CAI UM METEORO NA CABEÇA DO INIMIGO! EEEEEEE!
         Escreval ("VOCÊ VENCEU!")
         Escreval (nome, " salvou a Terra do terrível " ,inimigo)
         timer 1000
         Escreval ("FIM!")
fimse

                               //E com isso termina o tutorial de "COMO SER DOIDO IGUAL AO JOÃO"!
                               //espero ter ajudado e desculpem-me por não saber explicar direito
                               //Qualquer dúvida falem comigo no Face ou Whatsapp, vou tentar ficar online o máximo possível
         

//5 horas e meia pra chegar aqui!
fimalgoritmo
