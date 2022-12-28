#Escreva um programa que recebe como entradas (utilize a função input) 
# dois números inteiros correspondentes à largura e à altura de um retângulo, 
# respectivamente. O programa deve imprimir, usando repetições encaixadas (laços aninhados), 
# uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída.

from re import A

largura = int(input("Digite a largura do retangulo: "))
altura = int(input("Digite a altura do retangulo: "))

print(largura * '#')

alturaquant = altura - 1

while alturaquant != 0:
    print(largura * '#')
    alturaquant = alturaquant - 1