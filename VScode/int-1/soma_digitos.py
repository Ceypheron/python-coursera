numero = int(input("Digite o numero inteiro: "))
r = 0
while numero != 0:
    resto = numero % 10
    numero = (numero - resto)//10
    r = r + resto
final = r
print(final)