#Programa que lê o um conjunto de 100 números inteiros positivos e determina a quantidade de números pares e números ímpares.

def numeros():
    pares = 0
    impares = 0
    for i in range(1, 101):
        num = int(input())
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(pares)
    print(impares)

numeros()
    