#Programa desenvolvido por Lidiane Mel Loureiro em 2020
#Objetivo: Ensinar funções básicas do Python com o próprio programa como exemplo prático

#Criando as funções que serão usadas:
def Sumario() :
    print(" \n O que esse programa tem a ensinar:  ")
    print("##################### -SUMÁRIO- #####################")
    print("####        (1) O que é Python?                  ####")
    print("####        (2) Sintaxe básica                   ####")
    print("####        (3) Onde é usado?                    ####")
    print("####        (4) Exemplos/Apps                    ####")
    print("####        (5) Sair                             ####")
    print("#####################################################")
    
def parte1() :
    print("-------------------------------------------------")
    print("             - O que é Python? -                 ")
    print("-------------------------------------------------")
    print("Definição: Uma linguagem de programação.         ")
    print("Linguagem de Alto Nivel                          ")
    print("Desenvolvida em: 1992, por Guido Van Rossum      ")
    print("Empresa: Python Software Foundation              ")
    print("Obs: Este programa é desenvolvido em Python      ")
    print("-------------------------------------------------")

def parte2() :
    print("----------------------------------------------------")
    print("              - Sintaxe Básica -                    ")
    print("----------------------------------------------------")
    print("  Exibir mensagem na tela:  print("")               ")
    print("  Declarar uma variável:    variavel = i            ")
    print("  Fazer comentário:         #Comentário             ")
    print("  Entrada de dados:         input()                 ")
    print("  Fazer uma função:         def nome :              ")
    print("                                scripts             ")
    print("    Obs: Não usa ; ao final da linha                ")
    print("----------------------------------------------------")
    
def parte3() :
    print("-------------------------------------------------")
    print("               - Onde é usado? -                 ")
    print("-------------------------------------------------")
    print("    Desde de programas mais simples até os mais  ")
    print(" compleoxos. Python tem uma grande diversidade em")
    print(" suas programações, tendo várias fuções.         ")
    print("    Atualmente (2020), essa linguagem está sendo ")
    print(" usada com desenvolvimento de Inteligência Arti -")
    print(" ficial e para iniciantes na programação pela sua")
    print(" simplicidade.                                   ")

def parte4() :
    print("--------------------------------------------------")
    print("               - Exemplos -                       ")
    print("--------------------------------------------------")
    print(" -> Lista de Apps ou sites que foram desenvolvidos")
    print(" com a linguagem Python:                          ")
    print("\n 1- Instagram (Totalmente Python)               ")
    print(" 2-Google (Python nos Googlers)                   ")
    print(" 3-Spotify (Serviços interdependentes em Python)  ")
    print(" 4-Netflix (Bibliotecas Python)                   ")
    print(" 5-Uber (Python, Node.js, Go e Java)              ")
    print("--------------------------------------------------")

#Iniciando o programa com uma pergunta e usando input para pegar os dados:
print ("~Digite seu nome para continuar: ")
nome = input("> ")

#Exibindo dados do input junto do print:
print ("\n~*#####################################################~*")
print ("  Bem-Vindo", nome," ao Mundo Python! ")
print ("             Aproveite e divirta-se   ")
print ("~*#######################################################*~")

#Chamando a função Sumário:
Sumario()

#Exemplos de print e input
#Obs: \n é usado para dar espaço entre uma linha e outra
print("\n Deseja Continuar? \n 1-Sim \n 2-Não")
resposta = input("> ")

#Usando estrutura de decisão para responder de acoordo com a resposta do usuário:
if resposta == "1" :
    print("\n Obrigada por continuar! Vamos aos ensinamentos: \n")
    parte1() #Chamando as funções feitas no inicio do código(Linhas 15 a 62)
    parte2()
    parte3()
    parte4()
    print("################# DICA #################")
    print("##     Para você que se interessa     ##")
    print("##  pelo Python aqui vai uma dica,    ##")
    print("##  esse programa foi feito para      ##")
    print("##  te mostrar exemplos práticos      ##")
    print("##  sobre tudo o que foi ensinado     ##")
    print("##  aqui, então aproveite!            ##")
    print("########################################\n")

#Respondendo a 2º opção de resposta do usuário:
elif resposta == "2" :
    print("##  Que pena! Está perdendo um bom conteúdo inicial! ##\n")

#Mensagem de agradecimento antes de encerrar o programa:
print("#####################################")
print(" Obrigada pela sua atenção!          ")
print("     Espero que tenha ajudado!       ")
print("#####################################")