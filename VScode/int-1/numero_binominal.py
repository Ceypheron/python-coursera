def fatorial(n):
    fat = 1
    while (n > 1):
        fat = fat * n
        n = n - 1
    return fat

def numero_binomial(n,k):
    return fatorial(n) / (fatorial(k) * fatorial(n - k))

n = int(input("Digite o primeiro numero: "))
k = int(input("Digite o segundo numero: "))
print("O numero binominal e:",numero_binomial(n,k))