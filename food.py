import turtle as t
import random

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280,280)
        self.goto(x=rand_x, y=rand_y)
        self.refresh()
        
    def refresh(self):
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280,280)
        self.goto(x=rand_x, y=rand_y)
        
