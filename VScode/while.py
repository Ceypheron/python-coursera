operacao = int(input("Escolha que tipo de operação deseja realizar:\n1 para soma\n2 para multiplicacao\n3 para subtração\n4 para divisao\n"))
#soma
if operacao==1:
    quantidade = int(input("Digite a quantidade de numeros a serem somados: "))
    vsoma = 1
    rsoma = 0
    q = 0
    while q < quantidade:
        vsoma = float(input("Digite um valor a ser somado: "))
        rsoma = rsoma + vsoma
        q = q + 1
    print("O resultado da soma e: ",rsoma)
#multiplicação
if operacao==2:
    quantidade = int(input("Digite a quantidade de numeros"))
    vmultiplicacao = 1
    rmultiplicacao = 1
    q = 0
    while q < quantidade:
        vmultiplicacao = int(input("Digite um valor a ser multiplicado: "))
        rmultiplicacao = (rmultiplicacao * vmultiplicacao)
        q = q + 1
    print("O resultado da multiplicacao e: ",rmultiplicacao)
#divisao
if operacao==4:
    quantidade = int(input("Digite a quantidade de numeros a serem divididos: "))
    vdivisao = 1
    rdivisao = 0
    while quantidade != 0:
        vdivisao = float(input("Digite um vlaor a ser dividido: "))
        rdivisao = rdivisao / vdivisao
        quantidade = quantidade - 1
    print("O resultado da divisao e: ",rdivisao)
