import turtle as t 

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for postion in STARTING_POSITIONS:
            new_square = t.Turtle('square')
            new_square.color("white")
            new_square.penup()
            new_square.goto(postion)
            self.segments.append(new_square)

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y= self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_seg(self):
        x_pos = self.segments[-1].xcor()
        y_pos = self.segments[-1].ycor()
        new_square = t.Turtle('square')
        new_square.color("white")
        new_square.penup()
        new_square.goto(x=x_pos, y=y_pos)
        self.segments.append(new_square)

    def check_collison(self):
        # x = self.head.xcor()
        # y = self.head.ycor()
        for seg in self.segments[1:]: ##starts from the first body segment from index 1 of any list
            if self.head.distance(seg) < 10:
                return True
            
    def reset(self):
        for seg in self.segments:
            seg.goto(x=1000,y=1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
            
        return False

        

        



      