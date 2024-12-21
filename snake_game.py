import turtle as t
import snake
import time
import food
import scoreboard

screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# t = t.Turtle()
# t.setheading()
game = True

snake = snake.Snake()
food = food.Food()
scoreboard = scoreboard.Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def check_collsion_bounds(snake_head):
    width = screen.window_width() / 2
    height = screen.window_height() / 2

    x = snake_head.xcor()
    y = snake_head.ycor()

    if (x >= width or x <= -width):
        return True
    
    if (y >= height or y <= -height):
        return True
    
    return False

while game:
    screen.update()
    time.sleep(0.07)
    snake.move()

    if snake.head.distance(food) < 20:
        food.refresh()
        snake.add_seg()
        scoreboard.increase_score()

    if check_collsion_bounds(snake.head) == True:
        scoreboard.reset()
        snake.reset()

    if snake.check_collison() == True:
        scoreboard.reset()
        snake.reset()












screen.exitonclick()
