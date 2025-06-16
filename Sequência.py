#Programa que gera a sequência: 10, 20, 30, 40, ..., 990, 1000.

def sequencia():
    numeros = ""
    for i in range(10, 1001, 10):
        if i == 1000:
            numeros += f"{i}."
        else:
            numeros += f"{i}, "
    return numeros
    
print(sequencia())