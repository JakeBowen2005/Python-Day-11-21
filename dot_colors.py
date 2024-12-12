import colorgram
import turtle as t
import random

screen = t.Screen()
# Get screen dimensions
screen_width = screen.window_width()
screen_height = screen.window_height()

# Calculate bottom-left coordinates
_x = -screen_width // 4
_y = -screen_height // 4
# Extract colors from the image
colors = colorgram.extract('dot_colors.jpg', 30)  # Adjust the number of colors as needed

# Store the RGB values
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

for _ in range(3):
    del rgb_colors[0]

p = t.Turtle()
p.hideturtle()
p.speed("fast")
t.colormode(255)
p.penup()
screen.tracer(0)
p.goto(_x, _y)
screen.tracer(1)

for _ in range(10):
    for _ in range(10):
        p.dot(20, random.choice(rgb_colors))
        p.forward(50)
    _y = _y + 40
    p.goto(_x, _y)




screen.exitonclick()