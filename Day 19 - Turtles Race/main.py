from turtle import Turtle, Screen
import random

# Creating screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Declaring constant variables
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -100
is_race_on = False
all_turtles = []

# Creating Turtles
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    all_turtles.append(new_turtle)
    y_position += 30

# Users bet to start the game
if user_bet:
    is_race_on = True

# Starting the game
while is_race_on:
    for turtle in all_turtles:
        move_distance = random.randint(0,10)
        turtle.forward(move_distance)
        if turtle.xcor() > 240:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

screen.exitonclick()