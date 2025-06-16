#Programa que lê um número inteiro e mostra a soma dos dígitos para os números entre 0 (zero) e 100 mil ou -1 para outros valores.

n = int(input())

def inverso(numero):
    if 0 < n < 100000:
        cm = (numero) % 10
        numero = numero // 10
        dm = (numero) % 10
        numero = numero // 10
        u = (numero) % 10
        numero = numero // 10
        d = (numero) % 10
        numero = numero // 10
        c = (numero) % 10
        numero = numero // 10
        m = (numero) % 10
        numero = numero // 10
        invertido = cm + dm + u + d + c + m
        return invertido
    else:
        return -1

print (inverso(n))