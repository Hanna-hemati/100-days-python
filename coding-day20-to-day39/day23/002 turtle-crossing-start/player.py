import random
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start()
        self.setheading(90)

    def move_dis(self):
        self.forward(MOVE_DISTANCE)

    def start(self):
        self.goto(STARTING_POSITION)

    def is_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

