from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("*PONG PONG*")

ball = Ball()
paddle1 = Paddle((380, 0))
paddle2 = Paddle((-380, 0))

score = Score()

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(paddle1) < 50 and ball.xcor() > 340 or ball.distance(paddle2) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_pos()
        score.l_point()

    if ball.xcor() < -390:
        ball.reset_pos()
        score.r_point()


screen.exitonclick()
