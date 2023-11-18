from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 0.1
        self.new_x = random.choice([-10, 10])
        self.new_y = random.choice([-10, 10])

    def move(self):
        new_x = self.xcor() + self.new_x
        new_y = self.ycor() + self.new_y
        self.goto(new_x, new_y)

    def bounce(self):
        self.new_y *= -1

    def hit_paddle(self):
        self.new_x *= -1
        self.move_speed *= 0.95

    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.new_x *= -1
