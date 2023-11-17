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
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

    # Detect collision of the ball with the wall
    if abs(ball.ycor()) > 280:
        ball.bounce()
    # Detect collision of the ball with the Paddle
    if (ball.distance(right_paddle) < 30 and ball.xcor() >= 320) or (ball.distance(left_paddle) < 30 and ball.xcor() <=
                                                                     -320):
        ball.hit_paddle()

    if ball.xcor() >= 400:
        scoreboard.left_point()
        ball.reset_position()

    if ball.xcor() <= -400:
        scoreboard.right_point()
        ball.reset_position()

screen.exitonclick()
