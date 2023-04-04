# BackTracking
# Desenvolvido por: Yuri Getaruck
# RA: 2103303

matrizConeccoes = [[0, 100, 125, 100, 75],
                   [100, 0, 50, 75, 125],
                   [125, 50, 0, 100, 125],
                   [100, 75, 100, 0, 50],
                   [75, 125, 125, 50, 0]]

vertices = ["A", "B", "C", "D", "E"]


def converteLetraEmNumero(letra):
    switch = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
    }
    return switch.get(letra, "letra invalida")


def calculaDistancia(vetorResultado):

    resultadoApenasLetra = []
    for i in vetorResultado:
        resultadoApenasLetra.append(i.nome)

    distancia = 0

    print("Caminho encontrado entre " +
          resultadoApenasLetra[0] + " e " + resultadoApenasLetra[len(resultadoApenasLetra)-1] + ": ", end="")

    for i in range(len(resultadoApenasLetra)):
        if (i == 0):
            print(resultadoApenasLetra[i] + " -> ", end="")
        elif (i == len(resultadoApenasLetra) - 1):
            print(resultadoApenasLetra[i])
        else:
            print(resultadoApenasLetra[i] + " -> ", end="")

    for i in range(len(resultadoApenasLetra)-1):
        distancia += matrizConeccoes[converteLetraEmNumero(
            resultadoApenasLetra[i])][converteLetraEmNumero(resultadoApenasLetra[i+1])]
    return distancia


class Estado:

    def __init__(self, nome, pai):
        if (nome == "A" or nome == "B" or nome == "C" or nome == "D" or nome == "E"):
            self.nome = nome
            self.filhos = []
            self.pai = []

        for i in range(5):
            if (self.nome != vertices[i] and not (vertices[i] in self.pai)):
                self.filhos.append(vertices[i])

        self.pai.append(pai)


def busca_retrocesso(inicial, objetivo):
    listaEstados = [inicial]
    listaNovosEstados = [inicial]
    becoSemSaida = []
    estadoCorrente = inicial

    while (len(listaNovosEstados) > 0):

        if (estadoCorrente.nome == objetivo.nome):
            return listaEstados

        if (len(estadoCorrente.filhos) == 0):

            while ((len(estadoCorrente.filhos) != 0) and (estadoCorrente == listaEstados[0])):
                becoSemSaida.append(estadoCorrente)

                listaEstados.pop(0)

                listaNovosEstados.pop(0)

                estadoCorrente = listaNovosEstados[0]

                listaEstados.append(estadoCorrente)

        else:
            for filho in estadoCorrente.filhos:
                if (not (filho in becoSemSaida) and not (filho in listaEstados) and not (filho in listaNovosEstados)):
                    listaNovosEstados.append(
                        Estado(filho, estadoCorrente.pai + [estadoCorrente.nome]))

            listaNovosEstados.reverse()
            listaNovosEstados.pop()
            listaNovosEstados.reverse()

            estadoCorrente = listaNovosEstados[0]
            listaEstados.append(estadoCorrente)


controle = True

while (controle):

    print("Escolha um estado inicial entre A, B, C, D ou E, ou X para sair:")
    entrada1 = str(input())

    if (entrada1 == "X"):
        break

    print("Escolha outro estado entre A, B, C, D ou E: ")
    entrada2 = str(input())

    estado1 = Estado(entrada1, "X")
    estado2 = Estado(entrada2, "X")

    resultado = busca_retrocesso(estado1, estado2)

    print("\n\n")
    print("Distancia percorrida: " + str(calculaDistancia(resultado)))
    print("\n\n")
