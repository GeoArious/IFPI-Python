#Programa que lê o preço de um carro hoje e calcule em quantos meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o carro à vista.


preco_carro = float(input())
poupanca = 10000.0
rendimento_poupanca = 0.007
aumento_carro = 0.004
meses = 0

while poupanca < preco_carro:
    poupanca += poupanca * rendimento_poupanca
    preco_carro += preco_carro * aumento_carro
    meses += 1

print(meses)