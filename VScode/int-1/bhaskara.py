import math

def main():
    a = float(input("Qual o valor de a? "))
    b = float(input("Qual o valor de b? "))
    c = float(input("Qual o valor de c? "))
    imprime_raizes(a, b, c)

def delta(a, b, c):
    return (b**2)-4*a*c

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        print("A unica raiz e: ",raiz1)
    else:
        if d < 0:
            print("esta equacao nao possui raizes reais")
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            print("A primeira raiz e: ",raiz1)
            print("A segunda raiz e: ",raiz2)
main()