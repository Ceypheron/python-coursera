# lista de temperaturas
# retornar minima e maxima

def MinMax (temperaturas):
    print('A menor temperatura foi {}c'.format(minima(temperaturas)))
    print('A maior temperatura foi {}c'.format(maxima(temperaturas)))
############################################
def minima(temps):
    min = temps[0] 
    i = 1
    while i < len(temps):
        if temps[i] < min:
                min = temps[i]
        i = i + 1
    return min
###################################
def maxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max
##########################################
def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print('\nValor errado parra array {}'.format(temp))
        print('Valor esperado: {}\nValor calculado: {}'.format(valor_esperado,valor_calculado))
###############################################
def testa_minima():
    print('Iniciando os teste')
    teste_pontual([0],0)
    teste_pontual([0, 0, 0, 0, 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],0)
    teste_pontual([30, 22, 27, 25, 26, 27, 29, 31, 32, 33, 30, 24, 26, 27],22)
    teste_pontual([-15, -12, 0, 20, 30], -15)
    print('Teste finalizado')

MinMax([30, 22, 27, 25, 26, 27, 29, 31, 32, 33, 30, 24, 26, 27])