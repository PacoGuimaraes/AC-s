'''
Programação estruturada
11/03/24
AC 2
'''

def eq_seg_grau(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**(0.5)) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**(0.5)) / (2*a)
    return x1, x2

def bissexto(ano):
    resultado_ano = ( ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)
    return resultado_ano

def calcula_salario(valor_horas, num_horas):
    irpf = 0.275
    salario_bruto = valor_horas * num_horas
    imposto_renda = salario_bruto * irpf
    salario_liquido = salario_bruto - imposto_renda
    return salario_liquido
    
def main():
    print(eq_seg_grau(1,-6,8))
    print(bissexto(2000))
    print(calcula_salario(1200, 8))

main()

    