#verificar se o numero e primo e responder com TRUE/FALSE

def primo(x):
    div = 0
    for i in range(2, n):
        if (n % i == 0):
            div += 1
    if div == 0:
        return True
    else:
        return False

n = int(input("Digite um numero inteiro:  "))
while n > 0:
    if primo(n):
        print("{} e primo.".format(n))
    else:
        print("{} nao e primo".format(n))

    n = int(input("Digite um numero inteiro:  "))