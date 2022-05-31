# O projeto consiste em um jogo de advinhação,onde um número aleatório é gerado,o usuario começa com 1000 pontos,e a
# diferença do número chutado para o número secreto é reduzida dessa pontuação a cada rodada
import random


def jogar():
    print("*******************************")
    print("Bem vindo ao jogo de advinhação")
    print("*******************************")

    numero_secreto = random.randrange(1, 101)
    escolha = False
    pontos = 1000

    print("Qual será o nível de dificuldade")
    print("(1) Fácil (2) Médio (3) Difícil")

    while (escolha == False):
        nivel = int(input("Escolha o nível: "))
        if (nivel == 1):
            total_de_tentativas = 20
            escolha = True
        elif (nivel == 2):
            total_de_tentativas = 10
            escolha = True
        elif (nivel == 3):
            total_de_tentativas = 5
            escolha = True
        else:
            print("O número deve ser de 1 á 3")
            continue

    for atual in range(1, total_de_tentativas + 1):
        print(f"Tentativa {atual} de {total_de_tentativas}")
        chute_str = input("Digite um número entre 1 e 100 ")
        print("Você digitou", chute_str)
        chute_int = int(chute_str)

        if (chute_int < 1 or chute_int > 100):
            print("Digite um numero de 1 a 100")
            continue
        acertou = numero_secreto == chute_int
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        if (acertou):
            print(f"Você acertou,e ficou com {pontos} pontos")
            break

        else:
            if (maior):
                print("Você errou,o seu chute foi maior do que o número secreto")
            elif (menor):
                print("Você errou,o seu chute foi menor do que o número secreto")

            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos

    print("Fim de Jogo!")

if(__name__=="__main__"):
    jogar()

