#Programa que lê uma quantidade indefinida de números inteiros positivos terminada pelo número 0. Ao final, o programa mostra o maior e o menor de todos os números lidos.

numero = 0
maior = 0
menor = 0

while True:
    inserido = int(input())
    if inserido == 0:
        break
    else:
        if numero == 0:
            numero = inserido
            maior = inserido
            menor = inserido
        else:
            if inserido > maior:
                maior = inserido
            if inserido < menor:
                menor = inserido

print(maior)
print(menor)