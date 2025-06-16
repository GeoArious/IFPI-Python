#Programa que lê uma data no formado DDMMAAAA e informa se é uma data válida.

data = input()

def bissexto(ano):
    if ano % 4 != 0:
        return False
    
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    
def verificar(x):
    dia = int(x[:2])
    mes = int(x[2:4])
    ano = int(x[4:])

    if ano < 1 or mes < 1 or mes > 12 or dia < 1 or dia > 31:
        return False
    
    if mes in [4, 6, 9, 11] and dia > 30:
        return False
    
    if mes == 2:
        if bissexto(ano):
            if dia > 29:
                return False
        else:
            if dia > 28:
                return False

    return True    
    
print (verificar(data))