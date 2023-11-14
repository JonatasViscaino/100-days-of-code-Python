from turtle import Turtle, Screen
import random


# Function for colors:
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# Declaring pointer and screen
pointer = Turtle()
pointer.shape("circle")
pointer.speed("fastest")
pointer.hideturtle()
screen = Screen()
screen.colormode(255)

# Coordinates of pointer and n of dots
x_pos = -250
y_pos = -250
dots_per_line = 10
n_lines = 10

# Drawing painting
for _ in range(dots_per_line):
    pointer.penup()
    pointer.setposition(x_pos, y_pos)
    pointer.pendown()
    y_pos += 50
    for _ in range(n_lines):
        pointer.dot(20, random_color())
        pointer.penup()
        pointer.forward(50)
        pointer.pendown()

screen.exitonclick()
