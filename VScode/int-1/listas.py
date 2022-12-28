#listas

playlist = ['Scrim','Nirvana','BONES','White Buffalo','Hippie Sabotage']

print('Lista atual: {}'.format(playlist))

alterar = int(input('Deseja realizar alguma alteração?\n1 para sim\n2 para nao'))

if alterar == 1:
    playlist.append(input('O que deseja adicionar na playlist? '))
    print('Sua lista ficou:\n{}'.format(playlist))