from turtle import *

#uma função para desenhar um quadrado
#'def' significa 'define'
def drawSquare():
    pendown()
    begin_fill()
    for side in range(4):
        left(90)
        forward(50)
    end_fill()
    penup()

color("WhiteSmoke")
bgcolor("MidnightBlue")

drawSquare()
forward(100)
drawSquare()
left(90)
forward(180)

drawSquare()

hideturtle()
done()