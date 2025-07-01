from turtle import *
from random import *

#uma função para mover a tartaruga para uma posição aleatória
def moveToRandomLocation():
    penup()
    setpos( randint(-400,400), randint(-400,400) )
    pendown()

#uma função para desenhar uma estrela de um tamanho específico
def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()

#uma função para desenhar uma pequena galáxia de estrelas
def drawGalaxy(numberOfStars):
    starColours = ["#B0C5F9", "#2075A5", "#B872EF"]
    moveToRandomLocation()
    
    #desenha várias pequenas estrelas coloridas
    for star in range(numberOfStars):
        penup()
        left( randint(180,180) )
        forward( randint(5, 30) )
        pendown()
        
        #desenha uma pequena estrela de cor aleatória
        drawStar(7, choice(starColours))

#uma função para desenhar uma constelação de estrelas
def drawConstellation(numberOfStars):
    #moveToRandomLocation()

    #desenhar pontos finos, assim: *-*--*-*--*--*
    for star in range(numberOfStars - 1):
        drawStar(1, "white")
        penup()
        left( randint(-90,90) )
        forward( randint(20, 100) )
        pendown()

    #agora desenhando a última estrela
    drawStar( randint(7,15), "white")

speed(1)

#isso desenha um fundo azul escuro
bgcolor("MidnightBlue")

#desenha 30 estrelas brancas (tamanhos/posições aleatórias)
for star in range(30):
    moveToRandomLocation()
    drawStar( randint(5,25), "white")

#desenha 3 pequenas galáxias de 40 estrelas
for galaxy in range(3):
    drawGalaxy(40)

#desenha 2 constelações, cada uma com um número aleatório de estrelas
for constellation in range(2):
    drawConstellation(randint(4,7))

hideturtle()
done()