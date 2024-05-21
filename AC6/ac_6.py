'''
PROGRAMAÇÃO ESTRUTURADA
AC_6
PACO GUIMARÃES | 202402879669
25/03/2024

'''

# 1
print("Hello World!")

# 2
a = int(input())
b = int(input())
x = a + b
print("X =", x)

# 3
peca1 = input()
peca2 = input()
#
peca1 = peca1.split(" ")
peca2 = peca2.split(" ")
preco = int(peca1[1]) * float(peca1[2]) + int(peca2[1]) * float(peca2[2])
print(f"VALOR A PAGAR: R$ {preco:.2f}")

#4
abc = input()
abc = abc.split(" ")
#
a = int(abc[0])
b = int(abc[1])
c = int(abc[2])
#
ab = ((a+b+abs(a-b))/2)
ac = ((a+c+abs(a-c))/2)
bc = ((b+c+abs(b-c))/2)
#
if ab == ac:
    print(a, "eh o maior")
elif ab == bc:
    print(b, "eh o maior")
elif ac == bc:
    print(c, "eh o maior")

#5
a = input()
b = input()
#
a = a.split(" ")
b = b.split(" ")
#
ax = float(a[0])
ay = float(a[1])
#
bx = float(b[0])
by = float(b[1])
#
print(f"{(((bx - ax)**2) + ((by - ay)**2))**(1/2):.4}")