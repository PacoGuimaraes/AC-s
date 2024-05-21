'''
Programação Estruturada
18/03
AC_3
PACO MOREIRA SENRA GUIMARÃES
'''

def determina_tipo_triangulo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Não é um triângulo"
    elif a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def dia_semana(d):
    if d == 1:
        return "Domingo"
    elif d == 2:
        return "Segunda"
    elif d == 3:
        return "Terça"
    elif d == 4:
        return "Quarta"
    elif d == 5:
        return "Quinta"
    elif d == 6:
        return "Sexta"
    elif d == 7:
        return "Sabado"
    elif d <= 0 or d >= 8:
        return ""

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x, y):
    return x / y

def calculadora():
    x = float(input("Informe um número: "))
    y = float(input("Informe outro número: "))
    operacao = input("Informe a operação: ")
    if operacao == "soma":
        resultado  = soma(x, y)
    elif operacao == "subtracao":
        resultado = subtracao(x, y)
    elif operacao == "multiplicacao":
        resultado = multiplicacao(x, y)
    elif operacao == "divisao":
        resultado = divisao(x, y)
    else:
        resultado = "Operação invalida"
    print("Resultado: ", resultado)


def main():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo
    print("-" * 30)
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia
    print("-" * 30)
    calculadora()

main()
