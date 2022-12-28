#receber numero e verificar se e primo
def main():
    div = 0
    n = int(input("Digite um numero inteiro:  "))

    for i in range(2, n):
        if (n % i == 0):
            div += 1
            
    if div == 0:
        print("O numero digitado e primo.")
    else:
        print("O numero digitado nao e primo.")

main()