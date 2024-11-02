from turtle import *
import random

setup(600, 600)
bgcolor("white")
speed(200)
colormode(255)
pensize(1)

# 画气球
for i in range(8):
    # 随机起点
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    # 随机颜色
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




