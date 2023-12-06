from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375263"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Creating window object
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Creating text object
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 16, "bold"))
        self.score_label.grid(row=0, column=1)

        # Creating canvas object
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="test",
            width=280,
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Creating buttons object
        true_bt_img = PhotoImage(file="images/true.png")
        self.true_bt = Button(image=true_bt_img, highlightthickness=0, border=False, command=self.true_pressed)
        self.true_bt.grid(row=2, column=0)
        false_bt_img = PhotoImage(file="images/false.png")
        self.false_bt = Button(image=false_bt_img, highlightthickness=0, border=False, command=self.false_pressed)
        self.false_bt.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=f"{q_text}")
            self.buttons_state("active")
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the Quiz.")
            self.buttons_state("disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.buttons_state("disabled")

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.buttons_state("disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def buttons_state(self, state):
        self.true_bt.config(state=state)
        self.false_bt.config(state=state)
