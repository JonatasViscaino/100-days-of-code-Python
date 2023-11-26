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
km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)
equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(row=1, column=0)
km_result_label = Label(text="0", font=FONT)
km_result_label.grid(row=1, column=1)


# Button
def calculate_km():
    km_text = float(input_value.get())*1.60934
    km_result_label.config(text=f"{round(km_text,2)}")


calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(row=2, column=1)

# Entry
input_value = Entry(width=8)
input_value.focus()
input_value.grid(row=0, column=1)

window.mainloop()
