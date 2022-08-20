#Refaça o exercício 1 imprimindo os retângulos sem preenchimento, 
# de forma que os caracteres que não estiveremna borda do retângulo sejam espaços.

from re import L


largura = int(input("Digite a largura do retangulo: "))
altura = int(input("Digite a altura do retangulo: "))

i = 0
while i < altura:
    l = 0
    while l < largura:
        if i == 0 or i == altura - 1 or l == 0 or l == largura - 1:
            print("#"  ,end = "")
        else:
            print(" ",end = "")
        l = l + 1
    print()
    i = i + 1