#Programa que calcula o valor de H(H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n) com 4 (quatro) casas decimais.

n = int(input())

h = 0.0

for i in range(1, n + 1):
    h += 1 / i
print(f"{h:.4f}")