#Programa que lê o nome e o estado civil de uma pessoa, “1” para casado e “2” para solteiro. Se a pessoa for casada, ler também, o nome do cônjuge. Mostrar quantos caracteres no total existem no(s) nome(s) lido(s).
nome = input().strip()

ecivil = int(input())

nome2 = ""

quan2 = len(nome)

if ecivil == 1:
    nome2 = input().strip()
    quan1 = len(nome) + len(nome2)
    print (quan1)
else:
    print (quan2)