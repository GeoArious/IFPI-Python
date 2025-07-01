#Programa que lê a população de aves no início do ano 1600 e imprime, anualmente, a partir do fim de 1600, o número de nascimentos, mortes e o total da população por ano.

populacao = float(input())
dez_porcento = populacao // 10

ano = 1599

while populacao > dez_porcento:
    nascimentos = populacao * 0.01
    mortes = populacao * 0.06
    ano += 1
    populacao += nascimentos - mortes
    print(f"{ano},{nascimentos:.0f},{mortes:.0f},{populacao:.0f}")