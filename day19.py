import turtle as t

p = t.Turtle()
screen = t.Screen()
screen.listen()

def forward():
    p.forward(10)
def backward():
    p.backward(10)
def left():
    p.left(10)
def right():
    p.right(10)
def clear():
    t.clear()
    p.penup()
    p.home()
    p.pendown()
    p.clear()


screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=left, key="a")
screen.onkey(fun=right, key="d")
screen.onkey(fun=clear, key="c")






screen.exitonclick()