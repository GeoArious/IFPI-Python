#Programa que lê quantos metros a tartaruga sai à frente da lebre e calcule quantos minutos levará até que a lebre alcance a tartaruga.

distancia = int(input())

lebre = 0

tempo = distancia // 9
if distancia % 9 != 0:
    tempo += 1
print(tempo)