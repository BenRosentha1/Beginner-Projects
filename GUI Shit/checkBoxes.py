"""
This is a template for writing programs using tinkter.
"""
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import
from tkinter import *
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Window Declaration
root = Tk()
root.title("Title")
#root.iconbitmap("Location of ICO File")
root.geometry("750x450")


# Images


# Button Functionality
def enter():
    checkBoxes = [box1Var.get(), box2Var.get(), box3Var.get(), box4Var.get(), box5Var.get()]

    if not "off" in checkBoxes:
        print("You have selected box(es):", end=" ")
        totalBoxes = len(checkBoxes)
        for box in checkBoxes:
            if box != "off":
                print(str(box), end=" ")
    else:
        print("You have selected no boxes!")


# Buttons
enterBtn = Button(root, text="Enter", command=enter)


# Slider


# Checkboxes
box1Var = StringVar()
box2Var = StringVar()
box3Var = StringVar()
box4Var = StringVar()
box5Var = StringVar()

box1 = Checkbutton(root, text="This is box one!", variable=box1Var, onvalue="one", offvalue="off")
box2 = Checkbutton(root, text="This is box two!", variable=box2Var, onvalue="two", offvalue="off")
box3 = Checkbutton(root, text="This is box three!", variable=box3Var, onvalue="three", offvalue="off")
box4 = Checkbutton(root, text="This is box four!", variable=box4Var, onvalue="four", offvalue="off")
box5 = Checkbutton(root, text="This is box five!", variable=box5Var, onvalue="five", offvalue="off")


# Labels


# Pack it in
box1.pack()
box2.pack()
box3.pack()
box4.pack()
box5.pack()
enterBtn.pack()

# Main Loop
root.mainloop()