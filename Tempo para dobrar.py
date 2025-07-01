#Programa que pergunta o depósito inicial e a taxa de juros ao ano de uma poupança e depois mostra em quantos anos o valor acumulado será o dobro do valor inicial.

inicial = float(input())
taxa = float(input())

anos = 0
valor = inicial

while valor < 2 * inicial:
    valor += valor * (taxa / 100)
    anos += 1

print(anos)