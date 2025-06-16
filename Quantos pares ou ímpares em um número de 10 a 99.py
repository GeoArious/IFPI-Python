#Programa que lê um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o número lido: Nenhum dígito é ímpar; Apenas um dígito é ímpar; Os dois dígitos são ímpares.
n = int(input())

if n:
    numeros = str(n)
    impares = 0

    for d in numeros:
        if not int(d) % 2 == 0:
            impares += 1

if impares == 0:
    print ("Nenhum dígito é ímpar.")
elif impares == 1:
    print ("Apenas um dígito é ímpar.")
else:
    print ("Os dois dígitos são ímpares.")