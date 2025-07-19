import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("bisque3")
screen.tracer(0)

player = Player(())
car = CarManager()
score = Scoreboard

screen.listen()
screen.onkey(player.move_dis, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_car()
    for cars in car.all_cars:
        if cars.distance(player) < 25:
            game_is_on = False

    # seccess
    if player.is_finish():
        player.start()
        car.lvl_up()
        score.increase_lvl()


screen.exitonclick()
