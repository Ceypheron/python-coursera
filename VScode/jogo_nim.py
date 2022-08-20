
###########    
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n%(m+1) == 0:
        usuario_escolhe_jogada(n, m)
    else:
        computador_escolhe_jogada(n, m)
###########
def computador_escolhe_jogada(n,m):
    if n <= m:
        print("O computador removeu {} peças.".format(n))
        n = 0
        print("Fim de jogo! O computador ganhou!!")
        campeonato()
    else:
        for i in range (1, m):
            if (n%i) == 0:
                print("\n\nO computador removeu {} peças.".format(i))
                n = n - i
                print("Agora restam {} peças.".format(n))

                if n == 0:
                    print("Fim de jogo! O computador ganhou!!")
                    ncamp = 1
                    campeonato(ncamp)
                else:
                    usuario_escolhe_jogada(n, m)
###########
def usuario_escolhe_jogada(n, m):

    remover = int(input("\n\nQuantas peças você vai tirar? "))

    if remover > n or remover > m:
        remover = int(input("\nOops! Jogada inválida! Tente de novo:  "))
        computador_escolhe_jogada(n,m)
    else:
        n = n - remover
        print("Voce removeu {} peças, restam {} peças.\n".format(remover,n))
        computador_escolhe_jogada(n,m)
       
############
def campeonato(ncamp):
    ncamp = ncamp + 1
    if ncamp < 3:
        ncamp = ncamp + 1
        partida()
    else:
        print("----Final do campeonato----\n")
        print("Placar: Você 0 X 3 Computador")

partida()
