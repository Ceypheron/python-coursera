#Escreva a função maior_elemento que recebe
#como parâmetro uma lista com números inteiros e
# devolve um número inteiro correspondente ao maior 
# valor presente na lista recebida.

def maior_elemento(lista):
    m = 0
    for elemento in lista:
        if elemento > m:
            m = elemento
    return m
