from random import *

#essa variável guarda o número de vezes que o jogo já foi jogado
tentativas = 0

score = 0

#imprima as 3 portas e as instruções do jogo
print('''
Porta da Fortuna!
=========
      
Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!
  _______     _______     _______
 |       |   |       |   |       |
 |  [1]  |   |  [2]  |   |  [3]  |
 |   o   |   |   o   |   |   o   |
 |_______|   |_______|   |_______|

Escolha uma porta (1, 2 ou 3):
''')

#repetir, enquanto a variável score for menor do que 3
while score < 3:

    #soma 1 ao número de tentativas
    tentativas = tentativas + 1

    print("\nTentativa", tentativas, ":Escolha uma porta (1, 2 ou 3):")

#pegue a porta escolhida e a armazene como um número inteiro (int)
portaEscolhida = input()
portaEscolhida = int(portaEscolhida)

#escolha aleatoriamente a porta que esconde o prêmio (entre 1 e 3)
portaCerta = randint(1,3)

#mostre ao jogador qual porta ele escolheu e qual era a porta certa
print("A porta escolhida foi a", portaEscolhida)
print("A porta certa é a", portaCerta)

#o jogador ganha se o número da porta escolhida e o da porta certa forem o mesmo
if portaEscolhida == portaCerta:
    print("Parabéns!")
    score += 1
else:
    print("Que peninha!")

print("Sua pontuação é", score)

print("\n Você conseguiu! Terminou o jogo em", tentativas, "tentativas.")