"""
This is a user of the sliders in tkinter.
"""
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import
from tkinter import *
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Window Declaration
root = Tk()
root.title("Slider")
#root.iconbitmap("Location of ICO File")
root.geometry("750x450")


# Slider
vertical = Scale(root, from_=175, to=750)
horizontal = Scale(root, from_=201, to=1000, orient=HORIZONTAL)


# Images


# Button Functionality
def resize():
    x = horizontal.get()
    y = vertical.get()
    root.geometry(str(x) + "x" + str(y))

# Buttons
resizeBtn = Button(root, text="Resize", command=resize)

# Labels


# Pack it in
vertical.pack()
horizontal.pack()
resizeBtn.pack()

# Main Loop
root.mainloop()