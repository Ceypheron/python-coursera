#Como pedido na primeira video-aula desta 
# semana, escreva um programa que recebe uma 
# sequência de números inteiros e imprima todos 
# os valores em ordem inversa. A sequência sempre 
# termina pelo número 0. Note que 0 (ZERO) não deve 
# fazer parte da sequência.
def inverte():
    lista = []
    while True:
        n = int(input('Digite um numero: '))
        if (n != 0):
            lista.append(n)
        else:
            break
    lista.reverse()
    for l in lista:
        print(l)
inverte()