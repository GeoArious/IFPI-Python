#Programa que lê um número inteiro qualquer e mostre na forma invertida.

try:
    numero = input()
except EOFError:
    numero = ""

numero_invertido = ""
zero_à_esquerda = True

for digito in reversed(numero):
    if zero_à_esquerda and digito == "0":
        continue
    zero_à_esquerda = False
    numero_invertido += digito

if numero_invertido == "":
    print("0")
else:
    print(numero_invertido)