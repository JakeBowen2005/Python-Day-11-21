import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("High_score_data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0,y=275)
        self.write(arg=f"Score:  {self.score}  High Score: {self.high_score}", move=False, font=("Arial", 24, "normal"), align="Center")

    def changeScore(self):
        self.clear()
        self.write(arg=f"Score:  {self.score}   High Score: {self.high_score}", move=False, font=("Arial", 24, "normal"), align="Center")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("High_score_data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.changeScore()

    def increase_score(self):
        self.score += 1
        self.changeScore()

    # def GameOver(self):
    #     game_over = t.Turtle()
    #     game_over.penup()
    #     game_over.hideturtle()
    #     game_over.color("Green")
    #     game_over.write("Game Over", align="center", font=("Arial", 30, "normal"))