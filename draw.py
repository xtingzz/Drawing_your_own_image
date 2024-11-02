from turtle import *
import random

setup(600, 600)
bgcolor("white")
speed(200)
colormode(255)
pensize(1)

# draw ballons
for i in range(8):
    # start point
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    # color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color((r, g, b))
    begin_fill()
    circle(50)
    end_fill()

    # pencolor('black')
    circle(50)
    right(140)
    circle(60, 120)
    right(180)
    circle(40, -120)
    left(320)

    penup()
    goto(x, y)
    pendown()

exitonclick()




