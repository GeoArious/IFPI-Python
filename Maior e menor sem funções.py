#Programa que lê 5 números inteiros e escreva o maior e o menor deles.

v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
v5 = int(input())

if v1 > v2 and v1 > v3 and v1 > v4 and v1 > v5:
    print(v1)
elif v2 > v1 and v2 > v3 and v2 > v4 and v2 > v5:
    print(v2)
elif v3 > v2 and v3 > v1 and v3 > v4 and v3 > v5:
    print(v3)
elif v4 > v2 and v4 > v3 and v4 > v1 and v4 > v5:
    print(v4)
elif v5 > v2 and v5 > v3 and v5 > v4 and v5 > v1:
    print(v5)

if v1 < v2 and v1 < v3 and v1 < v4 and v1 < v5:
    print(v1)
elif v2 < v1 and v2 < v3 and v2 < v4 and v2 < v5:
    print(v2)
elif v3 < v2 and v3 < v1 and v3 < v4 and v3 < v5:
    print(v3)
elif v4 < v2 and v4 < v3 and v4 < v1 and v4 < v5:
    print(v4)
elif v5 < v2 and v5 < v3 and v5 < v4 and v5 < v1:
    print(v5)