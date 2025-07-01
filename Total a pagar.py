#Programa que lê o código e a quantidade de cada item comprado por um freguês, calcule e exiba o total a pagar.

total = 0

while True:
    codigo = str(input()).upper().strip()
    print("CÓDIGO  PRODUTO         PREÇO (R$)")
    print("H       Hamburger       5,50")
    print("C       Cheeseburger    6,80")
    print("M       Misto Quente    4,50")
    print("A       Americano       7,00")
    print("Q       Queijo Prato    4,00")
    print("X       PARA TOTAL DA CONTA")
    if codigo == "X":
        break
    if codigo == "H":
        total += 5.50
    elif codigo == "C":
        total += 6.80
    elif codigo == "M":
        total += 4.50
    elif codigo == "A":
        total += 7.00
    elif codigo == "Q":
        total += 4.00

print("%.2f" % total)