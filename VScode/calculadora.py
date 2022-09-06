operacao = int(input("Escolha que tipo de operação deseja realizar:\n1 para soma\n2 para multiplicacao\n3 para subtração\n4 para divisao\n"))

#soma
if operacao==1:

    quantidade = int(input("Digite a quantidade de numeros a serem somados: \n"))
    primeiro_resultado = int(input("Digite o valor a ser somado: \n"))
    restante_val = 0
    q = 1

    while q < quantidade:
        restante_val = float(input("Digite um valor a ser somado: \n"))
        primeiro_val = primeiro_val + restante_val
        q = q + 1

    print("O resultado da soma e: ",primeiro_resultado)

#multiplicação
if operacao==2:

    quantidade = int(input("Digite a quantidade de numeros:\n"))
    primeiro_resultado = int(input("Digite o valor a ser multiplicad: \n"))
    restante_val = 1
    q = 1

    while q < quantidade:
        restante_val = int(input("Digite um valor a ser multiplicado:\n "))
        primeiro_resultado = (primeiro_resultado * restante_val)
        q = q + 1

    print("O resultado da multiplicacao e: ",primeiro_resultado)

#divisao
if operacao==4:

    quantidade = int(input("Digite a quantidade de numeros a serem divididos:\n "))
    primeiro_resultado = int(input("Digite o valor a ser dividido:\n "))
    restante_val = 0
    q = 1

    while q < quantidade:
        restante_val = float(input("Digite um vlaor a ser dividido:\n "))
        primeiro_resultado = primeiro_resultado / restante_val
        q = q + 1

    print("O resultado da divisao e: ",primeiro_resultado)
