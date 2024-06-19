from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.config(padx= 25, pady=25)

def calculate():
    km = int(miles_input.get()) * 1.6093
    result_label.config(text= round(km))

miles_input = Entry(width= 10)
miles_input.insert(END, string="0")
miles_input.grid(column= 1, row = 0)

miles_label = Label(text="Miles")
miles_label.grid(column = 2, row = 0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column = 0, row = 1)

result_label = Label(text="0")
result_label.grid(column = 1, row = 1)

km_label = Label(text="KM")
km_label.grid(column = 2, row = 1)

calculate_button = Button(text="CALCULATE", command= calculate)
calculate_button.grid(column= 1, row = 2)





window.mainloop()