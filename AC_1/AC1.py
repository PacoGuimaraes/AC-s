'''
PROGRAMAÇÃO ESTRUTURADA
AC_1
PACO MOREIRA SENRA GUIMARÃES
MATRICULA: 202402879669

'''
def funcao_2_grau():
    a = int(input("Mande o parâmetro A :"))
    b = int(input("Mande o parâmetro B :"))
    c = int(input("Mande o parâmetro C :"))
    primeira_raiz = ((-b) + ((b**2 +(-4)*a*c)**(1/2))) /(2*a)
    segunda_raiz = ((-b) - ((b**2 +(-4)*a*c)**(1/2))) /(  2*a)
    print("A primeira raiz da equação é", primeira_raiz)
    print("A segunda raiz da equação é", segunda_raiz)

funcao_2_grau()

def ano_bissexto():
    ano = int(input("Qual ano?"))
    print((ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0))


ano_bissexto()


