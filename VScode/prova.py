from tkinter import N
def main():
    corretas = 0
    erradas = 0
        #question = input("What´s you name?\n").upper()
        #question = input("What´s you age?\n").upper()

    question = input("\n\nWhere do you live?\n").upper()
    if question != "I LIVE IN BOCAIUVA":
        print("Resposta errada!!")
        erradas = erradas + 1
    else:
        print("Resposta correta!!")
        corretas = corretas + 1

    question = input("\n\n\n").upper()
    if question != "":
        print("Resposta errada!!")
        erradas = erradas + 1
    else:
        print("Resposta correta!!")
        corretas = corretas + 1

    question = input("\n\n\n").upper()
    if question != "":
        print("\Resposta errada!!")
        erradas = erradas + 1
    else:
        print("Resposta correta!!")
        corretas = corretas + 1

        #possessive adjectives
        #nunbers and addresses
        #Modal verbs - may - could - can
        #might = pode ser ou talvez
        #interrogative pronouns
        #places in town I
    print("Resultado:\n{} acertos \n{} erros".format(corretas,erradas))

main()
