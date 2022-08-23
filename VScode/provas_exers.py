# lista de temperaturas
# retornar minima e maxima

def MinMax (temperaturas):
    print('A menor temperatura foi {}c'.format(minima(temperaturas)))
    print('A maior temperatura foi {}c'.format(maxima(temperaturas)))

def minima(temps):
    min = 0 
    i = 0
    while i < len(temps):
        if temps[i] < min:
                min = temps[i]
        i = i + 1
    return min

def testa_minima():

    print('Iniciando os teste')
    temp = [0]
    if minima(temp) != 0:
        print('Valor errado para array  {}'.format(temp))

    temp = [0,33,22,55,66,85,2,1,33,5,4,10,15,12,36,18,47]
    if minima(temp) != 0:
        print('Valor errado para array  {}'.format(temp))

    temp = [33,44,2,23,2,1,44,-2]
    if minima(temp) != -2:
        print('Valor errado para array  {}'.format(temp))

    print('Finalizando os teste')
testa_minima()