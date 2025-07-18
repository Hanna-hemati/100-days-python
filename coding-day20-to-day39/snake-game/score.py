from turtle import Turtle
ALIGNING = "center"
FONT = "Arial", 20, "normal"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 310)
        self.score_write()

    def score_write(self):
        self.write(f"SCORE: {self.score}", align=ALIGNING, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("#GAMEOVER#", align=ALIGNING, font=FONT)

    def inrease_score(self):
        self.score += 1
        self.clear()
        self.score_write()
