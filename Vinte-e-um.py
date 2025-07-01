#Jogo em que o objetivo é fazer exatamente 21 pontos.
from random import *

pontuacao = 0

# Instruções do jogo
print('''Vinte e Um!
===========================
Tente fazer exatamente 21 pontos!
''')

while jogando == True:

    numero = randint(1,10)
    print(f"\nSeu próximo número é {numero}")

    pontuacao += numero
    print(f"Sua pontuação atual é {pontuacao}")

    print("Gostaria de somar mais um número? (s/n)")
    resposta = input().lower()

    if resposta == 'n':
        print(f"Sua pontuação final é {pontuacao}")
        if pontuacao == 21:
            print("Parabéns! Você fez exatamente 21 pontos!")
        else:
            print("Poxa :( Você não fez 21 pontos.")
        jogando = False
