#

n = int(input("Digite um numero inteiro maior que 1: "))
fator = 2
multiplicidade = 0

while n > 1:
    while n % fator == 0:
        multiplicidade = multiplicidade + 1
        n = n / fator

    if multiplicidade > 0:
        print("O fator {} tem multiplicidade = {}".format(fator,multiplicidade))
        
    fator = fator + 1
    multiplicidade = 0