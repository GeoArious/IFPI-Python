#Programa que lê, separadamente, dia, mês e ano da data atual e, da mesma forma, a data de nascimento de uma pessoa, calcula e escreva a idade exata em anos.

dia = int(input())
mes = int(input())
ano = int(input())

d = int(input())
m = int(input())
a = int(input())

def c_idade():

    idade = ano - a

    if (mes, dia) < (m, d):
        idade -= 1

    print (idade)

c_idade()