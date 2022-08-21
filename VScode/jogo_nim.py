#########
def computador_escolhe_jogada(n, m):

    pcplay = 1

    while pcplay != m:
        if (n - pcplay) % (m+1) == 0:
            return pcplay
        else:
            pcplay += 1
    return pcplay
###############
def usuario_escolhe_jogada(n, m):

    jogadaV = False

    while not jogadaV:
        userplay = int(input('Quantas peças você vai tirar?\n'))
        if userplay > m or userplay < 1:
            print('\nOops! Jogada inválida! Tente de novo.')
        else:
            jogadaV = True
    return userplay
###############
def campeonato():

    numberround = 1

    while numberround <= 3:
        print('---- Rodada', numberround, '----')
        partida()
        numberround += 1

    print('\nPlacar: Você 0 X 3 Computador')
###############
def partida():

    n = int(input('Quantas peças?\n'))
    m = int(input('Limite de peças por jogada?\n'))

    PCjoga = False

    if n % (m+1) == 0:
        print('Voce começa!\n')
    else:
        print('Computador começa!\n')
        PCjoga = True

    while n > 0:
        if PCjoga:
            pcplay = computador_escolhe_jogada(n, m)
            n = n - pcplay
            if pcplay == 1:
                print('O computador tirou uma peça')
            else:
                print('\nO computador tirou', pcplay, 'peças')

            PCjoga = False
        else:
            userplay = usuario_escolhe_jogada(n, m)
            n = n - userplay
            if userplay == 1:
                print('Você tirou uma peça\n')
            else:
                print('Você tirou', userplay, 'peças\n')
            PCjoga = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.\n')
        else:
            if n != 0:
                print('Agora restam,', n, 'peças no tabuleiro.\n')

    print('Fim de jogo, o computador ganhou!')

print('Bem-vindo ao jogo nim')

modo = int(input('Escolha:\n1 - para jogar partida isolada\n2 - para jogar um campeonato\n'))

if modo == 2:
    print('Voce escolheu um campeonato!')
    campeonato()
else:
    if modo == 1:
        partida()