## fatorial com função


n = int(input("Digite um numero inteiro positivo: "))
n = 1
while n >= 0:
    f = 1
    while n > 1:
        f = f * n
        n = n - 1
    print(f)
    n = int(input("Digite um numero inteiro: "))

