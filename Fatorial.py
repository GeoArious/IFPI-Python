#Programa que calcula o fatorial de um número inteiro lido

n = int(input())

fatorial = 1

for i in range(1, n + 1):
    fatorial *= i
    
print(fatorial)