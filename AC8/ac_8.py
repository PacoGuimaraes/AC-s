"""
PROGRAMAÇÃO ESTRUTURADA
PACO GUIMARAES
AC7

"""

#1

def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

n_testes = int(input())

for i in range(n_testes):
    num = input()
    num = num.split()
    for i in range(len(num)):
        num[i] = int(num[i])

    num.sort()
    cont = mdc(num[0], num[1])

    print(cont)


#2

def min_movimentos_dama(x1, y1, x2, y2):
    # Se a dama já está na casa de destino, retorna 0
    if x1 == x2 and y1 == y2:
        return 0

    # Se a dama está na mesma linha, mesma coluna ou mesma diagonal, retorna 1
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return 1

    # Se não, retorna 2, pois em dois movimentos a dama pode chegar à casa de destino
    return 2

# Loop para processar os casos de teste
while True:
    x1, y1, x2, y2 = map(int, input().split())

    # Verifica se chegou ao final da entrada
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break

    # Calcula e imprime o mínimo de movimentos necessários
    print(min_movimentos_dama(x1, y1, x2, y2))


#3

while True:
    try:
        valores = input()
    except EOFError:
        break

    if valores.upper() == "EOF":
        break
    else:
        valores = valores.split()
        n1 = int(valores[0])
        n2 = int(valores[1])

        f1 = 1
        f2 = 1

        for i in range(n1, 1, -1):
            f1 *= i

        for i in range(n2, 1, -1):
            f2 *= i

        soma_fatoriais = f1 + f2
        print(soma_fatoriais)


#4

def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

while True:
    try:
        valores = input()
    except EOFError:
        break

    if valores.upper() == "EOF":
        break
    else:
        valores = valores.split()
        n1 = int(valores[0])
        n2 = int(valores[1])

        f1 = calcular_fatorial(n1)
        f2 = calcular_fatorial(n2)

        soma_fatoriais = f1 + f2
        print(soma_fatoriais)


#5

n_testes = int(input())
for _ in range(n_testes):
    qtd_comida = float(input())
    cont = 0
    while qtd_comida > 1:
        qtd_comida = qtd_comida*0.5
        cont += 1

    print(f"{cont} dias")


#6

entrada = int(input())
lista = []

for _ in range(entrada):
    num = int(input())
    lista.append(num)

contador = {}

for num in lista:
    if num in contador:
        contador[num] += 1
    else:
        contador[num] = 1

for i in sorted(contador.items()):
    print(f"{i[0]} aparece {i[1]} vez(es)")


#7

import math
import time

def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    N = int(input())
    for _ in range(N):
        X = int(input())
        start_time = time.time()
        result = "Prime" if is_prime(X) else "Not Prime"
        print(result)
        elapsed_time = time.time() - start_time
        if elapsed_time > 1:
            print("Tempo de execução excedeu 1 segundo.")
            break

if __name__ == "__main__":
    main()

#8

while True:
    N = int(input())
    if N == 0:
        break

    results = list(map(int, input().split()))

    mary_wins = results.count(0)
    john_wins = results.count(1)

    print(f"Mary won {mary_wins} times and John won {john_wins} times")


#9

def rafael(x, y):
    return (3 * x) ** 2 + y ** 2

def beto(x, y):
    return 2 * (x ** 2) + (5 * y) ** 2

def carlos(x, y):
    return -100 * x + y ** 3

qtd_testes = int(input())

for _ in range(qtd_testes):
    valores = input().split()
    x = int(valores[0])
    y = int(valores[1])

    r = rafael(x, y)
    b = beto(x, y)
    c = carlos(x, y)

    if r > b:
        if r > c:
            print("Rafael ganhou")
        else:
            print("Carlos ganhou")
    elif b > c:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")