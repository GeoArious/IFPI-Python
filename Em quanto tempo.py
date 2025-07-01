#Programa que lê a população de cada país e imprime o tempo necessário para que a população do país B ultrapasse a população do país A.

populacao_a = int(input())
populacao_b = int(input())

meses = 0

if populacao_a > populacao_b:
    while populacao_b <= populacao_a:
        populacao_a += int(populacao_a * 0.02)
        populacao_b += int(populacao_b * 0.03)
        meses += 1
else:
    while populacao_a <= populacao_b:
        populacao_a += int(populacao_a * 0.03)
        populacao_b += int(populacao_b * 0.02)
        meses += 1

print(meses)