"""
AC9
11/05/2024
PROGRAMAÇÃO ESTRUTURADA
PACO GUIMARÃES

"""

#1
n=int(input())
print(f"{n*2} minutos")

#2
from math import factorial as fat
print(fat(int(input())))

#3
N = int(input())

for _ in range(N):
    M = int(input())

    precos = {}

    for _ in range(M):
        fruta, preco = input().strip().split(' ')

        precos[fruta] = float(preco)

    P = int(input())

    resposta = 0.0
    for _ in range(P):
        fruta, quantidade = input().strip().split(' ')

        resposta += int(quantidade) * precos[fruta]

    print(f'R$ {resposta:.2f}')

#4
t = int(input())
x = list(map(int,input().split()))
print(x.count(t))

#5
c,p,f=map(int,input().split())
print("S") if c*f<=p else print("N")

#6
soma=0
for n in range(int(input())):
    horas,kmhora=map(int,input().split())
    soma+=(kmhora*horas)
print(soma)

#7
t = int(input())
t = t * 2 * 2
print(t)

#8
lista = []

for _ in range(int(input())):
    number = input()
    if not lista:
        lista.append(number)
    elif number != lista[-1]:
        lista.append(number)

print(len(lista))
