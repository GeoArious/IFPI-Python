#Programa que lê um conjunto 100 números inteiros e exibe o valor médio.

def numeros():
    soma = 0
    for i in range(1, 101):
        num = int(input())
        soma += num
    
    media = soma / 100

    return media

print('%.2f' %numeros())