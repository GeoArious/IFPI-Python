#Programa que lê um conjunto de números inteiros e exiba a soma dos mesmos.

inserido = 0
numero = 0

while True:
    inserido = int(input())
    if inserido == 0:
        break
    else:
        numero += inserido

print(numero)