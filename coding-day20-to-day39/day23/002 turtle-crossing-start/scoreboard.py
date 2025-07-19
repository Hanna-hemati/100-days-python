from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        # self.color("yellow")
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)
        self.update_score()

    def update_score(self):
        self.write(f"LEVEL: {self.lvl}", align="center", font=FONT)

    def increase_lvl(self):
        self.lvl += 1
        self.update_score()

