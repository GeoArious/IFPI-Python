#Programa que calcula a evolução de uma dívida no cartão de crédito e o crescimento salarial, mostrando quando os resultados se igualam.

salario = float(input())

divida = float(input())

mes = 10
ano = 2016

while True:
    divida = divida * 1.15
    
    mes += 1
    if mes > 12:
        mes = 1
        ano += 1

    
    if mes == 3:
        salario = salario * 1.05

    
    if divida > salario:
        print(f'{mes}/{ano}')
        break