from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Creating the screen object
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Creating the Paddles
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)

# Creating the Ball
ball = Ball()

# Creating the Scoreboard
scoreboard = Scoreboard()

# Controls of Paddles
screen.listen()
screen.onkeypress(right_paddle.turn_on_move_up, "Up")
screen.onkeypress(right_paddle.turn_on_move_down, "Down")
screen.onkeypress(left_paddle.turn_on_move_up, "w")
screen.onkeypress(left_paddle.turn_on_move_down, "s")
screen.onkeyrelease(right_paddle.stop, "Up")
screen.onkeyrelease(right_paddle.stop, "Down")
screen.onkeyrelease(left_paddle.stop, "w")
screen.onkeyrelease(left_paddle.stop, "s")

# Starting the game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Improve Paddle Movements
    if left_paddle.should_move_up:
        left_paddle.go_up()

    if right_paddle.should_move_up:
        right_paddle.go_up()

    if left_paddle.should_move_down:
        left_paddle.go_down()

    if right_paddle.should_move_down:
        right_paddle.go_down()

    # Detect collision of the ball with the wall
    if abs(ball.ycor()) > 280:
        ball.bounce()

    # Detect collision of the ball with the Paddle
    if ball.distance(right_paddle) < 40 and ball.xcor() > 320 and ball.new_x > 0:
        ball.hit_paddle()
    if ball.distance(left_paddle) < 40 and ball.xcor() < -320 and ball.new_x < 0:
        ball.hit_paddle()

    # Detect if the paddle right misses the ball
    if ball.xcor() >= 400:
        scoreboard.left_point()
        ball.reset_position()
    # Detect if the paddle left misses the ball
    if ball.xcor() <= -400:
        scoreboard.right_point()
        ball.reset_position()

screen.exitonclick()
