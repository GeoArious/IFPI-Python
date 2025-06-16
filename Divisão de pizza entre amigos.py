#Perguntar ao usuário quantas fatias de pizza tem e quantos amigos vão dividir a pizza. Mostrar quantas fatias cada um recebe e quantas sobram.
fatias = int(input().strip())
amigos = int(input().strip())

print (fatias//amigos)
print (fatias % amigos)