#Programa que lê um número inteiro e some 5 caso valor lido seja par ou some 8 caso o valor lido seja ímpar.

n = int(input())

def check():
    if n % 2 == 0:
        return n + 5
    else:
        return n + 8

print (check())