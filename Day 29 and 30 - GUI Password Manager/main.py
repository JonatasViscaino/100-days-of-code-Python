from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import string
import pyperclip


# Constants
INITIAL_EMAIL = "test@gmail.com"


# Buttons functions
def add_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showwarning(message="Please don't leave any empty fields!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


def generate_password():
    password_letters = [choice(string.ascii_letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(string.punctuation) for _ in range(randint(2, 4))]
    password_numbers = [choice(string.digits) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    final_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, final_password)
    pyperclip.copy(final_password)

# Creating window object
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, background="white")

# Creating canvas object
canvas = Canvas(width=200, height=200, background="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Creating Label objects
website_txt = Label(text="Website:", background="white")
website_txt.grid(row=1, column=0)
email_txt = Label(text="Email/Username:", background="white")
email_txt.grid(row=2, column=0)
password_txt = Label(text="Password:", background="white")
password_txt.grid(row=3, column=0)

# Creating Entries objects
website_entry = Entry(width=37, highlightbackground="white")
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=37, highlightbackground="white")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, INITIAL_EMAIL)
password_entry = Entry(width=21, highlightbackground="white")
password_entry.grid(row=3, column=1)

# Creating Buttons objects
generate_button = Button(text="Generate Password", width=11, highlightbackground="white", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=35, highlightbackground="white", command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
