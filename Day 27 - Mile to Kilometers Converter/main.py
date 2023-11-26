from tkinter import *

# Creating window object
window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

# Labels
FONT = ("Arial", 12)
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)
Km_label = Label(text="Km", font=FONT)
Km_label.grid(row=1, column=2)
equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(row=1, column=0)
result_label = Label(text="", font=FONT)
result_label.grid(row=1, column=1)

# Button
def calculate():
    km_text = float(input_value.get())*1.60934
    result_label.config(text=f"{km_text}")


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

# Entry
input_value = Entry(width=8)
input_value.focus()
input_value.grid(row=0, column=1)

window.mainloop()
