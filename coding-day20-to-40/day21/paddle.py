from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        paddle = Turtle()
        paddle.color("white")
        paddle.shape("rectangle")
        paddle.shapesize(20, 100)

