#Programa que lê o peso e a altura de uma pessoa, calcula o IMC, e depois, mostra uma mensagens:

peso = float(input())
altura = float(input())

imc = (peso) / (altura ** 2)

def mensagem():
    if imc < 18.5:
        return "Abaixo do peso"

    if 18.5 < imc < 25:
        return "Peso normal"

    if 25 < imc < 30:
        return "Sobrepeso"

    if 30 < imc < 35:
        return "Obeso leve"

    if 35 < imc < 40:
        return "Obeso moderado"

    if 40 <= imc:
        return "Obeso mórbido"

print(imc)

print (mensagem())