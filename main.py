from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(
    width= 300, 
    height = 200
    )
window.config(padx = 50, pady = 50)

equal_to_label = Label(
    text = "is equal to",
    font = ("Arial", 14)
    )
equal_to_label.grid(column = 0, row = 1)

distance_input = Entry(width= 20, font = ("Arial", 16))
distance_input.grid(
    column = 1, 
    row = 0
)

miles_label = Label(
    text = "Miles",
    font = ("Arial", 14)
)
miles_label.grid(
    column = 2, 
    row = 0
)

km_label = Label(
    text = "Km",
    font = ("Arial", 14)
)
km_label.grid(
    column = 2,
    row = 1
)

kilometer_conversion_label = Label(
    text = "0",
    font = ("Arial", 20)
)
kilometer_conversion_label.grid(
    column = 1,
    row = 1
)

def calculate_distance():
    miles_distance = int(distance_input.get())
    kilometer_distance = int(round(miles_distance * 1.609, 0))
    kilometer_conversion_label["text"] = str(kilometer_distance)

calculate_button = Button(
    text = "Calculate", 
    command = calculate_distance,
    font = ("Arial ", 16 )
)
calculate_button.grid(
    column  = 1, 
    row = 2
)





window.mainloop()
