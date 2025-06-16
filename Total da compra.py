#Programa que lê a quantidade de morangos e a quantidade de maças adquiridas e escreve o valor a ser pago pelo cliente

morango = float(input())

maca = float(input())

def valor(f1, f2):
    v1 = 2.5
    v2 = 1.8

    if f1 > 5:
        v1 = 2.2

    if f2 > 5:
        v2 = 1.5

    peso = f1 + f2

    total = (v1 * f1) + (v2 * f2)

    if peso > 8:
        total = total * 0.9

    return total

print ('%.2f' % valor(morango, maca))