import turtle as t
import random
import time


screen = t.Screen()
screen.setup(width=800, height=600)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

bet = screen.textinput(title="Bet",prompt="What color Turtle is your bet? ").lower()

for color in colors:
    new_turtle = t.Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color)
    turtles.append(new_turtle)
    new_turtle.shapesize(2)

x = -350
y = -150
for i in range(len(turtles)):
    turtles[i].goto(x=x, y=y)
    y += 75

race = True

while race:
    for i in range(len(turtles)):
        turtles[i].speed(random.randint(0,10))
        turtles[i].forward(random.randint(0,20))

        if turtles[i].xcor() > 400:
            winning_color = turtles[i].pencolor()
            if winning_color == bet:
                text = t.Turtle()
                text.hideturtle()
                text.penup()
                text.goto(x=-250,y=0)
                words = f"Your bet was correct {winning_color} won!!"
                for letter in words:
                    text.write(letter, align="center", font=("Arial", 24, "normal"))
                    text.forward(8)
                    time.sleep(0.05)
            else:
                text = t.Turtle()
                text.hideturtle()
                text.penup()
                text.goto(x=-250,y=0)
                words = f"Sorry your bet was incorrect {winning_color} won"
                for letter in words:
                    text.write(letter, align="center", font=("Arial", 24, "normal"))
                    text.forward(8)
                    time.sleep(0.05)
            race = False






screen.exitonclick()