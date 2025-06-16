#Programa que lê dois valores que correspondem à base e a altura de um retângulo. Verifica se os valores formam um retângulo ou um quadrado. Caso formem um quadrado imprime a palavra QUADRADO e caso seja um retângulo, mostra o perímetro e a área do retângulo.

v1 = int(input())
v2 = int(input())

def calculo(x, y):
    if x == y:
        return 'QUADRADO'
    else:
        p = (2 * x) + (2 * y)
        a = x * y
        return f'{p} - {a}'
    
print (calculo(v1, v2))