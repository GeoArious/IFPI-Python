#Programa que lê a altura e o sexo de uma pessoa, calcula e mostra o peso ideal.

altura = float(input())

sexo = int(input())

def ideal(n):
    if sexo == 1:
        return (72.7 * n) - 58
    else:
        return (62.1 * n) - 44.7
    
print ("%.2f" % ideal(altura))