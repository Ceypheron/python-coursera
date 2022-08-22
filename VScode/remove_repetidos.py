"""Escreva a função remove_repetidos que recebe como
parâmetro uma lista com números inteiros, verifica se tal
lista possui elementos repetidos e os remove. A função deve devolver
uma lista correspondente à primeira lista,
sem elementos repetidos. A lista devolvida deve estar ordenada."""

quantidade_numeros = int(input("Quantos numero deseja adicionar a lista?\n"))
lista = []

def remove_repetidos(lista):
    i = 0
    while i < quantidade_numeros:
        lista.append(int(input('Digite o numero a ser adicionado.  ')))
        i += 1
    lista = list(set(lista))
    return print(lista)

remove_repetidos(lista)