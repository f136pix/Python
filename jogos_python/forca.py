import random


def jogar():

    boas_vindas()
    palavra_secreta = palavra_escolhida()
    acertados = inicializa_palavra(palavra_secreta)
    print(acertados)

    enforcou = False
    acertou = False
    tentativas = 6


    while (not enforcou and not acertou):

        chute = numero_chutado()

        if (chute in palavra_secreta):
            chute_acertado(palavra_secreta,chute,acertados)

        else:
            tentativas -= 1
            desenha_forca(tentativas)

        if (tentativas < 0):
            enforcou = True

        acertou = "_" not in acertados

        print(acertados)

    if (acertou):
        imprime_ganhador()

    else:
        imprime_perdedor(palavra_secreta)

    print("Fim de jogo")



def boas_vindas():
    print("**************************")
    print("Bem vindo ao jogo de forca")
    print("**************************")

def palavra_escolhida():
    arquivos = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivos:
        linha = linha.strip()
        palavras.append(linha)
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_palavra(palavra):
    acertados = ["_" for letra in palavra]
    return acertados

def numero_chutado():
    chute = input("Chute uma letra ")
    chute = chute.strip().upper()
    return chute

def chute_acertado(palavra_secreta,chute,acertados):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            acertados[index] = letra

        index += 1

def imprime_ganhador():
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\:      /-.     ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \::.    /       ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")




def imprime_perdedor(palavra_secreta):
        print("Você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()





if (__name__ == "__main__"):
    jogar()