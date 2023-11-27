from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    timer_txt.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    canvas.itemconfig(count_txt, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 2 != 0:
        timer_txt.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif reps % 8 != 0:
        number_of_marks = int(reps / 2)
        check_marks.config(text=f"{number_of_marks * "✓"}")
        timer_txt.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        number_of_marks = int(reps / 2)
        check_marks.config(text=f"{number_of_marks * "✓"}")
        timer_txt.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        canvas.itemconfig(count_txt, text=f"{minutes}:0{seconds}")
    else:
        canvas.itemconfig(count_txt, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Creating Window object
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Creating Canvas object
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
count_txt = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Creating Buttons and Label Object
timer_txt = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
timer_txt.grid(row=0, column=1)
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
