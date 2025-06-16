#Programa que lê um número inteiro entre 100 e 999 e mostra quantos dígitos pares existem nesse número.
n = int(input())

if n:
    numeros = str(n)
    pares = 0

    for d in numeros:
        if int(d) % 2 == 0:
            pares += 1

    print(pares)