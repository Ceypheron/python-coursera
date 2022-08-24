# detector de plagio

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    comp_ass = 0
    for i in range(0,6):
        comp_ass = comp_ass + (abs(as_a[i] - as_b[i]))

    return comp_ass / 6
################################
 
################################
def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    setenca4 = 0 
    sentencas = separa_sentencas(texto)  
    soma_car_frase = 0
    palavasoma = 0 
    tam_meio_frase = 0
    frases = []
    palavras = []
    palavras2 = 0              
    sentenca2 = 0   
    sentenca3 = 0   
    tipo = 0    
    n = 0  
    ############################
    for sentenca in sentencas:      
        setenca4 = setenca4 + len(sentenca)        
        l_frases = separa_frases(sentenca)
        for f in l_frases:
            frases.append(f)
    for frase in frases:
        soma_car_frase = soma_car_frase + len(frase)
        l_pal = separa_palavras(frase)
        for palavra in l_pal:
            palavras.append(palavra)    
    for palavra in palavras:
        palavasoma = palavasoma + len(palavra)
##################################
    palavras2 = palavasoma/len(palavras)
    tipo = n_palavras_diferentes(palavras)/len(palavras)
    n = n_palavras_unicas(palavras)/len(palavras)
    sentenca2 = setenca4 / len(sentencas)
    sentenca3 = len(frases) / len(sentencas)
    tam_meio_frase = soma_car_frase / len(frases)

    return [palavras2, tipo, n, sentenca2, sentenca3, tam_meio_frase]
############################################################

############################################################
def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    init = []

    #####################
    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        init.append(compara_assinatura(ass_texto, ass_cp))
    m = init[0]
    ini = 1
    for i in range(1, len(init)):
        if (m > init[i]):
            ini = i
    return ini
###################################
def main():        
    assinatura = le_assinatura()
    textos = le_textos()
    p = avalia_textos(textos, assinatura)

    print('O autor do texto {} está infectado com COH-PIAH'.format(p))

main()