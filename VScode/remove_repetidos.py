#quantidade_numeros = int(input("Quantos numero deseja adicionar a lista?\n"))

def remove_repetidos(lista):
    lista = list(set(lista))
    lista.sort()
    return lista

lista = []

remove_repetidos(lista)