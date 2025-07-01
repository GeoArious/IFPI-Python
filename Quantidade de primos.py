#Programa que lê dois valores inteiros (x e y) e mostre todos os números primos entre x e y.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

x = int(input())
y = int(input())

for num in range(min(x, y), max(x, y) + 1):
    if is_prime(num):
        print(num)