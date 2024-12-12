import turtle as t
import random

screen = t.Screen()
screen.screensize(400, 400)

# colors = [
#     "red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "white",
#     "gray", "cyan", "magenta", "lime", "navy", "teal", "maroon", "olive", "gold", "violet"
# ]

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

speeds = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

angles = [0, 90, 180, 270]

p = t.Turtle()
p.pensize(5)

for _ in range(200):
    speed = random.choice(speeds)
    angle = random.choice(angles)
    p.setheading(angle)
    p.forward(30)
    p.color(random_color())
    p.speed(speed)
    

screen.exitonclick()