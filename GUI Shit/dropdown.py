"""
This is a dropdown menu.
"""
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import
from tkinter import *
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Window Declaration
root = Tk()
root.title("Dropdown")
#root.iconbitmap("Location of ICO File")
root.geometry("750x450")


# Dropdown
options=[
    "Select an Option",
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

selected = StringVar()
selected.set(options[0])
dropdown = OptionMenu(root, selected, *options)


# Images


# Button Functionality
def select(input):
    result = Label(root, text=str(input)).pack()


# Buttons
selectBtn = Button(root, text="Select", command=lambda: select(selected.get()))


# Labels


# Pack it in
dropdown.pack()
selectBtn.pack()

# Main Loop
root.mainloop()