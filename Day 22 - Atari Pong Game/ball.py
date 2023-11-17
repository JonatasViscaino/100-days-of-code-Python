from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.new_x = 10
        self.new_y = 10

    def move(self):
        new_x = self.xcor() + self.new_x
        new_y = self.ycor() + self.new_y
        self.goto(new_x, new_y)

    def bounce(self):
        self.new_y *= -1

    def hit_paddle(self):
        self.new_x *= -1

    def reset_position(self):
        self.home()
        self.hit_paddle()
