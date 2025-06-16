#Programa que simula o valor (com duas casas decimais) da prestação de uma compra parcelada sem juros de 1x até 24x.

valor = float(input())

def simular():
    for i in range(1, 25):
        parcela = valor / i
        print(f"{i}x de R$ {parcela:.2f}")

simular()