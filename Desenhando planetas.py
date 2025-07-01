from turtle import *

#uma função para desenhar um planeta de um tamanho específico
def drawPlanet(planetSize, planetColour):
    color(planetColour)
    pendown()
    begin_fill()
    circle(planetSize)
    end_fill()
    penup()

#isso desenha um fundo azul escuro
bgcolor("MidnightBlue")

#use a função para desenhar planetas de tamanhos diferentes!
drawPlanet(50, "Red")
forward(100)
drawPlanet(30, "White")

left(120)
forward(150)
drawPlanet(70, "Green")

hideturtle()
done()