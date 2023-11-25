from tkinter import *

# Creating window object
window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

# Button

def click():
    new_text = input.get()
    my_label.config(text=f"{new_text}")

button = Button(text="Click Me", command=click)
button.pack()

# Entry
input = Entry()
input.pack()




window.mainloop()

