import turtle
import pandas as pd


def write_state(state_name, x_location, y_location):
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()
    writer.goto(x_location, y_location)
    writer.write(f"{state_name}", align="center", font=("Arial", 10, "bold"))


# Setting up the screen and the background
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Opening the dataframe
df_state = pd.read_csv("50_states.csv")

# Game Set-up
already_guessed = []
while len(already_guessed) < 50:
    stated_guessed = screen.textinput(title=f"{len(already_guessed)}/50 Guess the State",
                                      prompt="What's another state's name?").title()
    if stated_guessed in df_state.state.values and stated_guessed not in already_guessed:
        row = df_state[df_state.state == stated_guessed]
        write_state(stated_guessed, row.x.iloc[0], row.y.iloc[0])
        already_guessed.append(stated_guessed)

    # Exit and create states to learn
    if stated_guessed == "Exit":
        states_to_learn = []
        for state in df_state.state.values:
            if state not in already_guessed:
                states_to_learn.append(state)
        df_states_to_learn = pd.DataFrame(states_to_learn)
        df_states_to_learn.to_csv("states_to_learn.csv")
        quit()

screen.exitonclick()
