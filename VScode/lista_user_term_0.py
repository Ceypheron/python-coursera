#usuario digita a lista com final 0 e depois a lista e impressa ao contrario


lista = []

while lista.append() != 0:
    lista.append(input('Qual valor deseja adicionar a lista?\n'))

tam = len(lista) - 1

while tam >= 0:
    print(lista[tam], end=", ")
    tam = tam - 1