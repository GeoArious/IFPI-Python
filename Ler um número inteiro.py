#Programa que lê um número inteiro menor que 1000 e mostra por extenso a quantidade de centenas, dezenas e unidades.

valor = int(input())

def separar(numero):
    u = (numero) % 10
    numero = numero // 10
    d = (numero) % 10
    numero = numero // 10
    c = (numero) % 10
    numero = numero // 10

    if c == 9:
        centena = "nove"
    elif c == 8:
        centena = "oito"
    elif c == 7:
        centena = "sete"
    elif c == 6:
        centena = "seis"
    elif c == 5:
        centena = "cinco"
    elif c == 4:
        centena = "quatro"
    elif c == 3:
        centena = "três"
    elif c == 2:
        centena = "duas"
    elif c == 1:
        centena = "uma"

    if c > 1:
        qcentena = "centenas"
    else:
        qcentena = "centena"

    if d == 9:
        dezena = "nove"
    elif d == 8:
        dezena = "oito"
    elif d == 7:
        dezena = "sete"
    elif d == 6:
        dezena = "seis"
    elif d == 5:
        dezena = "cinco"
    elif d == 4:
        dezena = "quatro"
    elif d == 3:
        dezena = "três"
    elif d == 2:
        dezena = "duas"
    elif d == 1:
        dezena = "uma"

    if d > 1:
        qdezena = "dezenas"
    else:
        qdezena = "dezena"

    if u == 9:
        unidade = "nove"
    elif u == 8:
        unidade = "oito"
    elif u == 7:
        unidade = "sete"
    elif u == 6:
        unidade = "seis"
    elif u == 5:
        unidade = "cinco"
    elif u == 4:
        unidade = "quatro"
    elif u == 3:
        unidade = "três"
    elif u == 2:
        unidade = "duas"
    elif u == 1:
        unidade = "uma"

    if u > 1:
        qunidade = "unidades"
    else:
        qunidade = "unidade"

    if c > 0 and d > 0 and u > 0:
        return f"{centena} {qcentena}, {dezena} {qdezena} e {unidade} {qunidade}."
    
    if c > 0 and d == 0 and u > 0:
        return f"{centena} {qcentena} e {unidade} {qunidade}."
    
    if c > 0 and d > 0 and u == 0:
        return f"{centena} {qcentena} e {dezena} {qdezena}."
    
    if c > 0 and d == 0 and u == 0:
        return f"{centena} {qcentena}."
    
    if c == 0 and d > 0 and u > 0:
        return f"{dezena} {qdezena} e {unidade} {qunidade}."
    
    if c == 0 and d > 0 and u == 0:
        return f"{dezena} {qdezena}."
    
    if c == 0 and d == 0 and u > 0:
        return f"{unidade} {qunidade}."
    
print (separar(valor))