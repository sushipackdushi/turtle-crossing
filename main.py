import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_left()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect collision with top of screen
    if player.ycor() > 280:
        player.reset()
        scoreboard.score_point()
        scoreboard.update()
        car_manager.level_up()


screen.exitonclick()