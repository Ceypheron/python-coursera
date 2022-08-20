

def maior_primo(numero):
    for n in reversed (range ( 1, numero + 1 )):
        if all(n % i != 0 for i in range (2,n)):
            return n
