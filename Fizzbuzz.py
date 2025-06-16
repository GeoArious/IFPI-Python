#Programa que lê um número inteiro positivo e escreva na tela: • FIZZ se o número é divisível por três; • BUZZ se o número é divisível por cinco; • FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo. • O próprio número caso não seja divisível por três ou por cinco.

n = int(input())

def mensagem(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FIZZBUZZ"
    elif x % 3 == 0:
        return "FIZZ"
    elif x % 5 == 0:
        return "BUZZ"
    else:
        return x

print (mensagem(n))