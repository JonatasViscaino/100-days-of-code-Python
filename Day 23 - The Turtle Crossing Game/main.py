import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Creating the screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing Game")
screen.tracer(0)

# Creating Objects
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

# Controls of Player
screen.listen()
screen.onkeypress(player.go_forward, "Up")
screen.onkeypress(player.go_backward, "Down")

# Starting the game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Generating and moving cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    # Detect successful crossing
    if player.check_finishline():
        scoreboard.increase_score()
        car_manager.level_up()

screen.exitonclick()
