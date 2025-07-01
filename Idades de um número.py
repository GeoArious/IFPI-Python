#programa que, para um número indeterminado de pessoas: lê a idade de cada pessoa, sendo que a leitura da idade 0 indica o fim dos dados e não deve ser considerada; calcula e escreve o número de pessoas; calcule e escreve a idade média do grupo; calcua e escreve a menor idade e a maior idade.

idade = 0
pessoas = 0
maior_idade = None
menor_idade = None

while True:
    inserido = int(input())
    if inserido == 0:
        break
    else:
        pessoas += 1
        idade += inserido
        if maior_idade is None or inserido > maior_idade:
            maior_idade = inserido
        if menor_idade is None or inserido < menor_idade:
            menor_idade = inserido

if pessoas > 0:
    idade_media = idade / pessoas
    print(pessoas)
    print("%.2f" % idade_media)
    print(menor_idade)
    print(maior_idade)
else:
    print(0)
    print(0)
    print(0)
    print(0)