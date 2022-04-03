def tabuleiro():
    print("+----+----+----+")
    print("| ", espacos[0], "| ", espacos[1], "| ", espacos[2], "|")
    print("+----+----+----+")
    print("| ", espacos[3], "| ", espacos[4], "| ", espacos[5], "|")
    print("+----+----+----+")
    print("| ", espacos[6], "| ", espacos[7], "| ", espacos[8], "|")
    print("+----+----+----+")

print("***********")
print("   Bem vindo ao jogo da velha!   ")
print("***********")
print("")
print("Esse jogo precisará de 2 jogadores")

espacos = [1,2,3,4,5,6,7,8,9]

xjogou = False
ojogou = False

velha = False

jogadas = 0

while(not velha):
    while(not xjogou):
        tabuleiro()
        jogadorX = int(input("Qual jogada você fará? [X]: "))

        if(jogadorX in espacos):
            for number in espacos:
                if(number == jogadorX):
                    espacos[number - 1] = "X"
            xjogou = True
            ojogou = False
        else:
            print("JOGADA INVÁLIDA")
            continue

    if(espacos[0] == "X" and espacos[4] == "X" and espacos[8] == "X"):
        tabuleiro()
        print("O JOGADOR X GANHOU!")
        velha = True
        break

    if (espacos[2] == "X" and espacos[4] == "X" and espacos[6] == "X"):
        tabuleiro()
        print("O JOGADOR X GANHOU!")
        velha = True
        break

    if (espacos[0] == "X" and espacos[1] == "X" and espacos[2] == "X"):
        tabuleiro()
        print("O JOGADOR X GANHOU!")
        velha = True
        break

    if (espacos[3] == "X" and espacos[4] == "X" and espacos[5] == "X"):
        tabuleiro()
        print("O JOGADOR X GANHOU!")
        velha = True
        break

    if (espacos[6] == "X" and espacos[7] == "X" and espacos[8] == "X"):
        tabuleiro()
        print("O JOGADOR X GANHOU!")
        velha = True
        break

    if (espacos[0] == "X" and espacos[3] == "X" and espacos[6] == "X"):
        tabuleiro()
        print("O JOGADOR X GANHOU!")
        velha = True
        break

    if (espacos[1] == "X" and espacos[4] == "X" and espacos[7] == "X"):
        tabuleiro()
        print("O JOGADOR X GANHOU!")
        velha = True
        break

    if (espacos[2] == "X" and espacos[5] == "X" and espacos[8] == "X"):
        tabuleiro()
        print("O JOGADOR X GANHOU!")
        velha = True
        break

    for number in espacos:
        if(number == "X" or number == "O"):
            jogadas += 1
    if(jogadas == 9):
        tabuleiro()
        print("DEU VELHA!")
        velha = True
        break
    jogadas = 0


    while(not ojogou):
        tabuleiro()
        jogadorO = int(input("Qual jogada você fará? [O]: "))

        if(jogadorO in espacos):
            for number in espacos:
                if(number == jogadorO):
                    espacos[number - 1] = "O"
            ojogou = True
            xjogou = False
        else:
            print("JOGADA INVÁLIDA")
            continue

    if(espacos[0] == "O" and espacos[4] == "O" and espacos[8] == "O"):
            tabuleiro()
            print("O JOGADOR O GANHOU!")
            velha = True
            break

    if (espacos[2] == "O" and espacos[4] == "O" and espacos[6] == "O"):
        tabuleiro()
        print("O JOGADOR O GANHOU!")
        velha = True
        break

    if (espacos[0] == "O" and espacos[1] == "O" and espacos[2] == "O"):
        tabuleiro()
        print("O JOGADOR O GANHOU!")
        velha = True
        break

    if (espacos[3] == "O" and espacos[4] == "O" and espacos[5] == "O"):
        tabuleiro()
        print("O JOGADOR O GANHOU!")
        velha = True
        break

    if (espacos[6] == "O" and espacos[7] == "O" and espacos[8] == "O"):
        tabuleiro()
        print("O JOGADOR O GANHOU!")
        velha = True
        break

    if (espacos[0] == "O" and espacos[3] == "O" and espacos[6] == "O"):
        tabuleiro()
        print("O JOGADOR O GANHOU!")
        velha = True
        break

    if (espacos[1] == "O" and espacos[4] == "O" and espacos[7] == "O"):
        tabuleiro()
        print("O JOGADOR O GANHOU!")
        velha = True
        break

    if (espacos[2] == "O" and espacos[5] == "O" and espacos[8] == "O"):
        tabuleiro()
        print("O JOGADOR O GANHOU!")
        velha = True
        break