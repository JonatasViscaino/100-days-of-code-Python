from tkinter import *
import pandas as pd
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# Getting data from csv file
current_card = {}
to_learn_dict = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except pd.errors.EmptyDataError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn_dict = original_data.to_dict(orient="records")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn_dict = original_data.to_dict(orient="records")
else:
    to_learn_dict = data.to_dict(orient="records")


# Button function
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(to_learn_dict)
    except IndexError:
        current_card = {"French": "félicitations", "English": "Congratulations"}
    finally:
        canvas.itemconfig(card_image, image=front_img)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=f"{current_card['French']}", fill="black")
        flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=flip_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="white")


def is_known():
    try:
        to_learn_dict.remove(current_card)
    except ValueError:
        print("Game Finish!")
    else:
        new_data = pd.DataFrame(to_learn_dict)
        new_data.to_csv("data/words_to_learn.csv", index=False)
        next_card()


# Creating window object
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Creating canvas object
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
flip_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Creating buttons object
right_bt_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_bt_img, highlightthickness=0, bd=0, height=95, width=95, command=is_known)
right_button.grid(row=1, column=1)
wrong_bt_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_bt_img, highlightthickness=0, bd=0, height=95, width=95, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
