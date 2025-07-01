#Programa que lê uma quantidade indefinida de números inteiros positivos terminada pelo número 0 (zero).Ao final, o programa mostra a média aritmética de todos os números lidos (excluindo o zero).

numero = 0
contador = 0

while True:
    inserido = int(input())
    if inserido == 0:
        break
    else:
        numero += inserido
        contador += 1


print("%.2f" % (numero / contador))