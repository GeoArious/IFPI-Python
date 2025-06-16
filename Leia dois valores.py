#Programa que lê dois valores e uma das seguintes operações será executada: 1 – Adição; 2 – Subtração; 3 – Multiplicação; 4 – Divisão.

n1 = int(input())
n2 = int(input())
n3 = int(input())

def calcular(x, y, z):
    if z == 1:
        resultado = x + y
    elif z == 2:
        resultado = x - y
    elif z == 3:
        resultado = x * y
    elif z == 4:
        resultado = x / y

    return "%.2f" % resultado

print (calcular(n1, n2, n3))