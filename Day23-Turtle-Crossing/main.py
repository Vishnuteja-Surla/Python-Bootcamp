import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

screen.update()

game_is_on = True

car_count = 0

while game_is_on:

    time.sleep(0.1)
    screen.update()

    if car_count == 6:
        car_manager.create_car()
        car_count = 0
    else:
        car_count += 1
    car_manager.move()

    if player.finish_line():
        player.restart()
        scoreboard.increment_score()
        car_manager.speed_up()

    for i in car_manager.cars:
        if player.distance(i) < 20:
            game_is_on = False
            scoreboard.game_over()
            break

screen.exitonclick()