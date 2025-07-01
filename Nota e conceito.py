#Programa que lê a nota de um aluno, entre zero e dez. Mostra a mensagem “Nota inválida.” caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. Após informar uma nota válida, o aluno apresenta o conceito.

while True:
    nota = float(input())
    if 0 <= nota <= 10:
        if nota >= 8.5:
            conceito = "A"
        elif nota >= 7:
            conceito = "B"
        elif nota >= 5:
            conceito = "C"
        elif nota >= 4:
            conceito = "D"
        else:
            conceito = "E"
        print(conceito)
        break
    else:
        print("Nota inválida.")