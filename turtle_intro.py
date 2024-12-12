import turtle as t

# Setup the screen and turtle
screen = t.Screen()
screen.screensize(800, 600)

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.penup()

# Disable animation
screen.tracer(0)

# Move the turtle to the far left
timmy.goto(-200, 0)

# Re-enable animation
screen.tracer(1)

# Create the dashed line
for _ in range(5):
    timmy.forward(20)
    timmy.penup()
    timmy.forward(20)
    timmy.pendown()

# Exit on click
screen.exitonclick()
