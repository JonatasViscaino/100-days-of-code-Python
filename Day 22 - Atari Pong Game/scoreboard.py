from turtle import Turtle
FONT = ("Courier", 50, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{self.left_score}", align="center", font=FONT)
        self.goto(100, 250)
        self.write(f"{self.right_score}", align="center", font=FONT)

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()