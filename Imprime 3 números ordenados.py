#Programa que lê três números por parâmetro e mostra na tela em ordem crescente.
n1 = int(input())
n2 = int(input())
n3 = int(input())

numeros = [n1, n2, n3]

numeros.sort()

print(numeros[0])
print(numeros[1])
print(numeros[2])