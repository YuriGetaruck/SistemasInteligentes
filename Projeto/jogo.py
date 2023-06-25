import random


def criaVetorDePalavras():
    file = open('palavras1.txt')

    palavrasTodas = file.readlines()

    for i in range(len(palavrasTodas)):
        palavrasTodas[i] = palavrasTodas[i].strip()

    palavrasCom5Letras = []

    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in palavrasTodas:
        if (len(i) == 5):
            palavrasCom5Letras.append(i.upper())

    for i in palavrasCom5Letras:
        for letra in i:
            letra.lower()
            if (not (letra.lower() in alfabeto)):
                palavrasCom5Letras.remove(i)

    return palavrasCom5Letras


palavras = criaVetorDePalavras()

print(palavras)
