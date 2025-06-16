#Programa que emite uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito", entre 3 ou 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

p1 = input().upper().strip()
p2 = input().upper().strip()
p3 = input().upper().strip()
p4 = input().upper().strip()
p5 = input().upper().strip()

def suspeito():

    n = 0

    if p1 == "S":
        n = n + 1

    if p2 == "S":
        n = n + 1

    if p3 == "S":
        n = n + 1

    if p4 == "S":
        n = n + 1

    if p5 == "S":
        n = n + 1

    if n == 2:
        return 'Suspeito'
    elif n == 3 or n == 4:
        return 'Cúmplice' 
    elif n == 5:
        return 'Assassino'
    else:
        return 'Inocente'
    
    
print (suspeito())