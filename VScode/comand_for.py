
playlist = ['Nirvana','BONES','Scrim']


for musics in playlist:
    print('Curto {}'.format(musics))

add_quantidade = int(input("Quantas musicas deseja adicionar a lista? "))

for i in range (0,add_quantidade):
    playlist.append(input("Qual musico deseja adiciona?\n"))

print("A playlist ficou:\n{}".format(playlist))