import turtle as t

screen = t.Screen()
screen.screensize(400, 400)

p = t.Turtle()

#triangle
for _ in range(3):
    p.forward(100)
    p.right(120)

p.color("red")
#square
for _ in range(4):
    p.forward(100)
    p.right(90)
p.color("blue")

for _ in range(5):
    p.forward(100)
    p.right(72)
p.color("green")

for _ in range(6):
    p.forward(100)
    p.right(60)
p.color("purple")

for _ in range(7):
    p.forward(100)
    p.right(51.4285714)
p.color("yellow")

for _ in range(8):
    p.forward(100)
    p.right(45)
p.color("orange")

for _ in range(9):
    p.forward(100)
    p.right(40)
p.color("brown")

for _ in range(10):
    p.forward(100)
    p.right(36)



screen.exitonclick()

