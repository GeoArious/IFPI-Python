#Programa que lê a data de nascimento, digitada no formado ddmmaaaa (um número inteiro com 8 dígitos), e mostra o seu número da sorte.


data_nascimento = int(input())

digitos = list(str(data_nascimento))

soma = 0
for d in digitos:
    soma += int(d)

print(soma)