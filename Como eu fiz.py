print('''
Q1 - No Python, como se chama uma 'caixa' usada para armazenar dados?
      a - texto
      b - variável
      c - uma caixa de sapatos
''')
resposta = input().lower()

score = 0

if resposta == "a":
    print(" Não - texto é um tipo de dado :( ")
elif resposta == "b":
    score = score + 1
    print(" Correto!! :) ")
elif resposta == "c":
    print(" Não seja bobinho! :( ")
else:
    print(" Você não escolheu a, b ou c :( ")

print('''
Q2 - No Python, qual a função usada para imprimir algo na tela?
      a - print
      b - input
      c - upper
''')
resposta2 = input().lower()

if resposta2 == "a":
    score = score + 1
    print(" Correto!! :) ")
elif resposta2 == "b":
    print(" Não :( ")
elif resposta2 == "c":
    print(" Errado :( ")
else:
    print(" Você não escolheu a, b ou c :( ")

print('''
Q3 - No Python, qual sinal de pontuação é usado para inserir textos?
      a - aspas ("")
      b - traço (-)
      c - ponto final(.)
''')
resposta3 = input().lower()

if resposta3 == "a":
    score = score + 1
    print(" Correto!! :) ")
elif resposta3 == "b":
    print(" Errado :( ")
elif resposta3 == "c":
    print(" Não :( ")
else:
    print(" Você não escolheu a, b ou c :( ")

print("Seu score é: ", score)

if score == 3:
    print("Muito bem!")
else:
    print("Tente novamente...")