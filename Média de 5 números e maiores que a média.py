#Programa que lê 5 números inteiros, calcula e mostre a média e escreve os que são maiores que a média.
def valor(n, media):
    if n > media:
        return True
    else:
        return False 

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

media = (n1 + n2 + n3 + n4 + n5) / 5
print ("%.2f" % media)

if valor(n1, media):
    print (n1)

if valor(n2, media):
    print (n2)

if valor(n3, media):
    print (n3)

if valor(n4, media):
    print (n4)

if valor(n5, media):
    print (n5)
