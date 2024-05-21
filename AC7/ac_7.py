"""
PROGRAMAÇÃO ESTRUTURADA
AC7
PACO GUIMARÃES

"""

#1

salario_base =float(input())

if salario_base<= 400:
    reajuste = 15
elif salario_base > 400 and salario_base <= 800:
    reajuste = 12
elif salario_base > 800 and salario_base <= 1200:
    reajuste = 10
elif salario_base > 1200 and salario_base <= 2000:
    reajuste = 7
elif salario_base > 2000:
    reajuste = 4

salario_novo = salario_base * (reajuste*0.01) + salario_base

print(f"Novo salario: {salario_novo:.2f}")
print(f"Reajuste ganho: {salario_base * (reajuste*0.01):.2f}")
print(f"Em percentual: {reajuste} %")

#2

cont = 0
for _ in range(5):
    temp = int(input())
    if temp%2 == 0:
        cont += 1

print(f"{cont} valores pares")

#3

cont = 0
x = int(input())
y = int(input())

if x > y:
    a = y
    b = x
else:
    a = x
    b = y

for i in range(a,b+1):
    if i%13 == 0:
        pass
    else:
        cont += i

print(cont)

#4

posicao0 = int(input())

vetor = [0]*10
vetor[0] = posicao0

for i in range(1,10):
    vetor[i] = vetor[i-1]*2

for _ in range(10):
    print(f"N[{i}] = {vetor[i]}")

#5

tamanho = int(input())
valores = [int(x) for x in input().split()]

menor = valores[0]
posicao = 0

for i in range(1, tamanho):
    if valores[i] < menor:
        menor = valores[i]
        posicao = i

print("Menor valor:", menor)
print("Posicao:", posicao)


#6

coluna = int(input())
operacao = input().upper()

matriz = []
for _ in range(12):
    linha = []
    for _ in range(12):
        temp = float(input())
        linha.append(temp)
    matriz.append(linha)



soma = 0

for i in range(12):
    soma += matriz[i][coluna]

if operacao == 'M':
    media = soma / 12
    print(f'{media:.1f}')
elif operacao == 'S':
    print(f'{soma:.1f}')


#7

n_testes = int(input())
for i in range(n_testes):
    string_lida = input()
    lista_string_lida = string_lida.split(" ")
    lista_ordenada = sorted(lista_string_lida, key=len, reverse=True)
    print(" ".join(lista_ordenada))