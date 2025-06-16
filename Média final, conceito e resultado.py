#Programa que lê o número de matrícula de um aluno, suas notas em 3 provas e a média das notas obtidas nos exercícios e calcula a média final.

matricula = input()

n1 = float(input())
n2 = float(input())
n3 = float(input())
m = float(input())

mf = (n1 + (n2 * 2) + (n3 * 3) + m) / 7

def final(mf):
    if mf >= 9:
        return "A"
    elif 9 > mf >= 7.5:
        return "B"
    elif 7.5 > mf >= 6.0:
        return "C"
    elif 6.0 > mf >= 4.0:
        return "D"
    elif mf < 4.0:
        return "E"

def resultado(mf):
    nota_final = final(mf)
    if nota_final in ["A", "B", "C"]:
        return "Aprovado"
    else:
        return "Reprovado"

print(matricula)
print("%.2f" % mf)
print(final(mf))
print(resultado(mf))
