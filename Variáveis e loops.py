lados = 4
angulo = 360 / lados

from turtle import *

speed(11)
shape("turtle")
pensize(6)
color("Red")

for count in range(36):
    forward(100)
    left(angulo)


done()