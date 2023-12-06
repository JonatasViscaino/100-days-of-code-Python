from tkinter import *

THEME_COLOR = "#375263"


class QuizInterface:

    def __init__(self):
        # Creating window object
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Creating text object
        self.score_label = Label(text="score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Creating canvas object
        self.canvas = Canvas(width=300, height=250)
        self.canvas.create_text(150, 125, text="test", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Creating buttons object
        true_bt_img = PhotoImage(file="images/true.png")
        self.true_bt = Button(image=true_bt_img, highlightthickness=0, border=False)
        self.true_bt.grid(row=2, column=0)
        false_bt_img = PhotoImage(file="images/false.png")
        self.false_bt = Button(image=false_bt_img, highlightthickness=0, border=False)
        self.false_bt.grid(row=2, column=1)


        self.window.mainloop()
