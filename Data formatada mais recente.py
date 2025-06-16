#Programa que lê 2 datas e escreva qual delas é a mais recente.

dia = int(input())
mes = int(input())
ano = int(input())

d = int(input())
m = int(input())
a = int(input())

def data(dia, mes, ano):
    return(f"{dia}/{mes}/{ano}")

if (ano, mes, dia) > (a, m, d):
    print(data(dia, mes, ano))
else:
    print(data(d, m, a))