from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("*Snake Game*")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # snake eats food
    if snake.segment[0].distance(food) < 20:
        food.refresh()
        snake.extened_snke()
        score.inrease_score()
    # snake touches and losses
    if snake.segment[0].xcor() > 340 or snake.segment[0].xcor() < -340 or snake.segment[0].ycor() > 340 or snake.segment[0].ycor() < -340:
        game_is_on = False
        print("You LOSE!!")
        score.game_over()

screen.exitonclick()
