from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Creating the screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Creating snake and food from their Classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Controls of Snake
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

# game speed control
sleep_time = 0.1

# Starting the game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        sleep_time *= 0.95

    # Detect collision with wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
