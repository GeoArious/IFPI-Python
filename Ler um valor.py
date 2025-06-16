#Programa que lê um número inteiro e calcula o resto da divisão inteira do número lido por 5, depois, de acordo com o resultado da divisão: Se 0, escreve o resultado da equação 9n + 7, onde n é o valor lido; Se 1, escreve se o valor lido é par ou ímpar; Se 2, escreve o resultado da equação 5n2 – 3n + 42, onde n é o valor lido; Se 3, escreve a divisão inteira do valor lido por 10; Se 4, escreve o quadrado do valor lido;

valor = int(input())

def calculo(n):
    resultado = n % 5

    if resultado == 0:
        return 9 * n + 7
    
    if resultado == 1:
        return 'par' if n % 2 == 0 else 'ímpar'
    
    if resultado == 2:
        return (5 * n ** 2) - (3 * n) + 42
    
    if resultado == 3:
        return n // 10
    
    if resultado == 4:
        return n ** 2
    
print (calculo(valor))