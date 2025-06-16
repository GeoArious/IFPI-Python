#Programa que lê 3 números inteiros e escreva uma das mensagens a seguir, de acordo com os valores lidos: Todos os valores são diferentes; Existem dois valores iguais e um diferente; Todos os valores são iguais.

n1 = int(input())
n2 = int(input())
n3 = int(input())

def valores(x, y, z):
    if x == y == z:
        return 'Todos os valores são iguais'
    elif x == y or x == z or y == z:
        return 'Existem dois valores iguais e um diferente'
    else:
        return 'Todos os valores são diferentes'
    
print(valores(n1, n2, n3))