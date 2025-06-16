#Programa que lê um conjunto de 100 números inteiros positivos e determina o maior deles.

def numeros():
    maior = 0
    for i in range(100):
        numero = int(input())
        if numero > maior:
            maior = numero

    return maior

print(numeros())