from ssl import HAS_NEVER_CHECK_COMMON_NAME


def main():
    def imc():
        altura = float(input("Qual a sua altura? Ex: 1.60\n"))
        peso = float(input("Qual seu peso ?\n"))
        altura = altura**2
        imc = peso / altura
        print ("\n\nSeu IMC e: ",imc)

    def ficha():
        tsegunda = input("Qual sera o treino na segunda?\n")
        tterca = input("Qual sera o treino na terça?\n")
        tquarta = input("Qual sera o treino na quarta?\n")
        tquinta = input("Qual sera o treino na quinta?\n")
        tsexta = input("Qual sera o treino na sexta?\n")
        tsabado = input("Qual sera o treino no sabado?\n")

        print("\n\n----Sua ficha de treino----\nsegunta: {}\nterça: {}\nquarta: {}\nquinta: {}\nsexta: {}\nsabado: {}\n".format(tsegunda,tterca,tquarta,tquinta,tsexta,tsabado))

    def dieta():
        taxabasal = 0
        peso = int(input("Qual o seu peso?\n"))
        idade = input("Qual sua idade?\n")
        sexo = input("Qual o seu sexo:\n 1 para homem\n2 para mulher")
        if sexo == 2 and 18 < idade >= 10 :
            taxabasal = (13,3 * peso) + 692


    opcao = int(input("Ola o que deseja?\nTecle 1 para IMC\nTecle 2 para ficha de treino\n"))
    if opcao == 1:
        imc()
    else:
        ficha()

main()