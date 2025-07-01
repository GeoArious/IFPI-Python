from turtle import *
from random import *

# uma função para mover a tartaruga para uma posição aleatória
def moveToRandomLocation():
    penup()
    setpos(randint(-400, 400), randint(-400, 400))
    pendown()

# uma função para desenhar um triângulo de um tamanho específico
def drawTriangle(triangleSize, triangleColour):
    color(triangleColour)
    pendown()
    begin_fill()
    for side in range(3):
        forward(triangleSize)
        left(120)
    end_fill()
    penup()

# uma função para desenhar um pequeno grupo de triângulos
def drawTriangleGroup(numberOfTriangles):
    triangleColours = ["#B0C5F9", "#2075A5", "#B872EF"]
    moveToRandomLocation()
    for _ in range(numberOfTriangles):
        penup()
        left(randint(180, 180))
        forward(randint(5, 30))
        pendown()
        drawTriangle(15, choice(triangleColours))

# uma função para desenhar uma "constelação" de triângulos
def drawTriangleConstellation(numberOfTriangles):
    for _ in range(numberOfTriangles - 1):
        drawTriangle(10, "white")
        penup()
        left(randint(-90, 90))
        forward(randint(20, 100))
        pendown()
    drawTriangle(randint(15, 30), "white")

speed(1)
bgcolor("MidnightBlue")

# desenha 30 triângulos brancos (tamanhos/posições aleatórias)
for _ in range(30):
    moveToRandomLocation()
    drawTriangle(randint(10, 40), "white")

# desenha 3 grupos de 40 triângulos coloridos
for _ in range(3):
    drawTriangleGroup(40)

# desenha 2 constelações de triângulos, cada uma com um número aleatório de triângulos
for _ in range(2):
    drawTriangleConstellation(randint(4, 7))

hideturtle()
done()