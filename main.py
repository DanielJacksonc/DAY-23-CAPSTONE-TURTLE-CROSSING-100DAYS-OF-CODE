import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
player.player()
car = CarManager()
score = Scoreboard()



screen.listen()
screen.onkey(player.player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()
        if player.ycor() > 280:
            score.level_increase()
            player.starting_position()
            car.increase_speed()

            # game_is_on = False









screen.exitonclick()