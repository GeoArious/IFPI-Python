#Programa que lê 3 valores inteiros, determina se é o segundo ou o terceiro valor lido que possui menor diferença com relação ao primeiro, imprimindo o valor da diferença.

v1 = int(input())
v2 = int(input())
v3 = int(input())

def diferenca(x, y, z):
    if x > y:
        d1 = x - y
    else:
        d1 = y - x

    if x > z:
        d2 = x - z
    else:
        d2 = z - x

    return d1 if d1 < d2 else d2
    
print (diferenca(v1, v2, v3))