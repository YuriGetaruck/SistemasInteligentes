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


def verificar_palpite(palpite, palavra):

    tentativas = 0
    acertos = list()
    letrasUtilizadas = list()

    if (len(palpite) != 5):
        print("\npalavra invalida\n")
        return acertos

    if (not (palpite in criaVetorDePalavras())):
        print("\npalavra invalida\n")
        return acertos

    letras_palavra = list(palavra)
    letras_palpite = list(palpite)

    for i in range(len(letras_palpite)):
        if (not (letras_palpite[i] in letrasUtilizadas)):
            letrasUtilizadas.append(letras_palpite[i])
            letrasUtilizadas.sort()
        if letras_palpite[i] == letras_palavra[i]:
            acertos.insert(i, "C")
        elif letras_palpite[i] in letras_palavra:
            acertos.insert(i, "E")
        else:
            acertos.insert(i, "_")

    print("acertos: ", end="")

    for i in acertos:
        print(i, end="")
    print()
    print(letrasUtilizadas)

    if palpite == palavra:
        print("acertou")
        return acertos
    elif tentativas >= 6:
        print("perdeu")
        return acertos


def jogo():
    # Gera palavras possiveis e seleciona uma
    palavra = random.choice(criaVetorDePalavras())
    # recebe_palpite
    controle = True
    while (controle):
        palpite = input("palpite: ")
        palpite = palpite.upper()
        acertos = verificar_palpite(palpite, palavra)
        buscaPalavra(palavra, acertos)
        if (acertos == "CCCCC"):
            controle = False


def buscaPalavra(palavra, certos):
    bancoPalavras = criaVetorDePalavras()
    melhoresProximasPalavras = list()
    contemAsLentras = list()

    for i in range(len(palavra)):
        if ((certos[i] == "C") or (certos[i] == "E")):
            contemAsLentras.append(palavra[i])
            print(contemAsLentras)


def main():
    jogo()


main()


# imoplementar AG para solucionar o jogo
