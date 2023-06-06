"""
This is a simple Calculator that implements tkinters functionality to create a GUI.
"""
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import
from tkinter import *
from tkinter import messagebox as mb
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Window Declaration
root = Tk()
root.title("Calculator")
#root.iconbitmap("C:\\Users\\benmr\\OneDrive\\Documents\\GitHub\\Beginner-Projects\\GUI Shit")

frameMain = LabelFrame(root, padx=5, pady=5)
frameMain.pack()

r = StringVar()

def checkAnswer(submittion):
    match submittion:
        case "DOOR":
            inText = "I'm sorry that is incorrect!"
            name = "Incorrect"
        case "WHEEL":
            inText = "Way to go!  You're one of the smart ones!"
            name = "Correct"

    resultLabel = mb.showinfo(name, inText)

# Labels
questionLabel = Label(frameMain, text="In the entire world, what are there more of?").pack()

# Buttons
Radiobutton(frameMain, text="Doors!", variable=r, value="DOOR").pack()
Radiobutton(frameMain, text="Wheels!", variable=r, value="WHEEL").pack()
submitButton = Button(frameMain, text="Submit Answer", command=lambda: checkAnswer(r.get())).pack()

# Main Loop
root.mainloop()
