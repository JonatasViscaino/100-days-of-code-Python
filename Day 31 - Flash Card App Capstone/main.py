from tkinter import *

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# Creating window object
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Creating canvas object
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_img)
canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="trouve", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Creating buttons object
right_bt_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_bt_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
right_button.grid(row=1, column=0)
wrong_bt_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_bt_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=1)

window.mainloop()
