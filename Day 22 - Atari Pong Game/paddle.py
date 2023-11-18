from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x_cor, y_cor)
        self.should_move_up = False
        self.should_move_down = False

    def turn_on_move_up(self):
        self.should_move_up = True

    def turn_on_move_down(self):
        self.should_move_down = True

    def stop(self):
        self.should_move_up = False
        self.should_move_down = False

    def go_up(self):
        new_y = self.ycor() + 20
        if self.ycor() < 250:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if self.ycor() > -240:
            self.goto(self.xcor(), new_y)
