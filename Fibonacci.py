#Programa que lê um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci.

n = int(input())

a, b = 0, 1

for i in range(n):
    if i < n - 1:
        print(a, end=', ')
    else:
        print(a)
    a, b = b, a + b