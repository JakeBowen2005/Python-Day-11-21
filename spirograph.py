import turtle as t
import random

screen = t.Screen()
screen.screensize(400, 400)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

t.speed("fastest")
for _ in range(120):
    t.circle(150)
    t.color(random_color())
    t.left(3)








screen.exitonclick()