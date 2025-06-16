from turtle import *

qual = int(input("Digite 1 para pentágono, 2 para hexágono e 3 para circulo: "))

def pentagono():
    if qual == 1:
        speed(5)
        shape("turtle")

        for count in range(5):
            right(72)
            forward(100)

        done()

    elif qual == 2:
        speed(5)
        shape("turtle")

        for count in range(6):
            right(60)
            forward(100)

        done()

    elif qual == 3:
        speed(300)
        shape("turtle")

        for count in range(360):
            right(1)
            forward(1)

        done()

    else:
        print("Opção inválida. Por favor, digite 1 ou 2.")

pentagono()