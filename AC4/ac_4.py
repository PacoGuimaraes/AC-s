'''
AC4 Programação estruturada
05/03/2024
'''

def le_nome():
    return input("Informe o seu nome: ")


def ler_notas():
    ap1 = float(input("Nota da AP1: "))
    ap2 = float(input("Nota da AP2: "))
    as1 = float(input("Nota da AS: "))
    ac = float(input("Nota da AC: "))
    return ap1, ap2, as1, ac

def validar_notas(ap1, ap2, as1, ac):
    if ap1 < 0 or ap1 > 10:
        return False
    elif ap2 < 0 or ap2 > 10:
        return False
    elif as1 < 0 or as1 > 10:
        return False
    elif ac < 0 or ac > 10:
        return False
    return True

def maior_nota(ap1, ap2, as1):
    if as1 > ap2:
        return ap1, as1
    if as1 > ap1:
        return as1, ap2
    return ap1, ap2

def calcular_media(n1, n2, ac):
    return (n1 + n2) * 0.4 + ac * 0.2


def informar_aprovacao(media):
    print(media)
    if media >= 7:
        print("Aprovado!")
    else:
        print("Reprovado!")



def main():
    nome = le_nome()
    if nome:
        ap1, ap2, as1, ac = ler_notas()
        if validar_notas(ap1, ap2, as1, ac):
            n1, n2 = maior_nota(ap1, ap2, as1)
            media = calcular_media(n1, n2, ac)
            informar_aprovacao(media)

main()

