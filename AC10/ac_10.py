"""
PACO GUIMARÃES
PROGRAMAÇÃO ESTRUTURADA
AC10

"""

#1

class Camiseta:
    def __init__(self, n, c, t):
        self.nome = n
        self.cor = c
        self.tamanho = t


def comp(a, b):
    if(a.cor == b.cor):
        if(a.tamanho == b.tamanho):
            if(a.nome < b.nome):
                return -1
            if(a.nome > b.nome):
                return 1
            return 0
        if(a.tamanho > b.tamanho):
            return -1
        return 1
    if(a.cor < b.cor):
        return -1
    return 1


#2

import sys
from collections import defaultdict

def main():
    entrada = sys.stdin.read
    linhas = entrada().strip().split("\n")

    posicao = 0
    casos = int(linhas[posicao])
    posicao += 1

    for caso in range(casos):
        if caso > 0:
            print()

        contagem_arvores = defaultdict(int)
        total_arvores = 0

        while posicao < len(linhas) and linhas[posicao].strip() == '':
            posicao += 1

        while posicao < len(linhas) and linhas[posicao].strip() != '':
            arvore = linhas[posicao].strip()
            contagem_arvores[arvore] += 1
            total_arvores += 1
            posicao += 1

        for nome_arvore in sorted(contagem_arvores):
            porcentagem = (contagem_arvores[nome_arvore] / total_arvores) * 100
            print(f"{nome_arvore} {porcentagem:.4f}")

if __name__ == "__main__":
    main()


#3

import math
while True:
    try:
        degraus = int(input())
        h, c, l = input().split()

        hipotenusa = math.sqrt((int(c) ** 2) + (int(h) ** 2))
        hipotenusa *= (int(l)/100*int(degraus))/100
        print('%.4f'%hipotenusa)

    #Até eu descobrir como fazia isso aq...
    except EOFError:
        break