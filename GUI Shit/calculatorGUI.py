"""
This is a simple Calculator that implements tkinters functionality to create a GUI.
"""
#-----------------------------------------------------------------------
# Import
from tkinter import *
#-----------------------------------------------------------------------
# Window Declaration
root = Tk()
root.title("Calculator")
root.iconbitmap("C:\\Users\\benmr\\OneDrive\\Documents\\GitHub\\Beginner-Projects\\GUI Shit")

# Button Functionality
def click(num):
    current = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, str(current) + str(num))

def clickMultiply():
    current = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, str(current) + "*")

def clickDivide():
    current = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, str(current) + "/")

def clickSubtract():
    current = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, str(current) + "-")

def clickFrontP():
    current = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, str(current) + "(")

def clickBackP():
    current = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, str(current) + ")")

def clickDot():
    current = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, str(current) + ".")

def clickBksp():
    inputBox.delete(len(inputBox.get())-1, END)

def clickAns():
    pass

def clickAdd():
    current = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, str(current) + "+")

def clickClr():
    inputBox.delete(0, END)

def clickEquals():
    pass

def clickExp():
    current = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, str(current) + "^")

def clickPi():
    current = inputBox.get()
    inputBox.delete(0, END)
    inputBox.insert(0, str(current) + "π")

def clickMoveRight():
    pass

def clickMoveLeft():
    pass

def clickSquared():
    pass


# Buttons
one = Button(root, text = "1", command=lambda: click(1), padx=22, pady=20)
two = Button(root, text = "2", command=lambda: click(2), padx=22, pady=20)
three = Button(root, text = "3", command=lambda: click(3), padx=22, pady=20)
four = Button(root, text = "4", command=lambda: click(4), padx=22, pady=20)
five = Button(root, text = "5", command=lambda: click(5), padx=22, pady=20)
six = Button(root, text = "6", command=lambda: click(6), padx=22, pady=20)
seven = Button(root, text = "7", command=lambda: click(7), padx=22, pady=20)
eight = Button(root, text = "8", command=lambda: click(8), padx=22, pady=20)
nine = Button(root, text = "9", command=lambda: click(9), padx=22, pady=20)
zero = Button(root, text = "0", command=lambda: click(0), padx=22, pady=20)
dot = Button(root, text = ".", command=lambda: clickDot, padx=23, pady=20)
ans = Button(root, text = "Ans", command=clickAns, padx=15, pady=20)
equals = Button(root, text = "=", command=clickEquals, padx=23, pady=20)
clr = Button(root, text = "Clr", command=clickClr, padx=18, pady=20)
bksp = Button(root, text = "Bksp", command=clickBksp, padx=13, pady=20)
frontP = Button(root, text = "(", command=clickFrontP, padx=7.5, pady=20)
backP = Button(root, text = ")", command=clickBackP, padx=7.5, pady=20)
exp = Button(root, text = "^", command=clickExp, padx=21, pady=20)
multiply = Button(root, text = "*", command=lambda: click(), padx=23, pady=20)
divide = Button(root, text = "/", command=clickDivide, padx=22, pady=20)
add = Button(root, text = "+", command=clickAdd, padx=21, pady=20)
subtract = Button(root, text = "-", command=clickSubtract, padx=23, pady=20)
pi = Button(root, text = "pi", command=clickPi, padx=22, pady=20)
moveRight = Button(root, text = ">", command=clickMoveRight, padx=7, pady=20)
moveLeft = Button(root, text = "<", command=clickMoveLeft, padx=7, pady=20)
squared = Button(root, text = "x^2", command=clickSquared, padx=17, pady=20)

# Input Box
inputBox = Entry(root, width=35, borderwidth=5)


# Pack it in
inputBox.grid(row=0, column=0, columnspan=8)
dot.grid(row=6, column=0, columnspan=2)
zero.grid(row=6, column=2, columnspan=2)
ans.grid(row=6, column=4, columnspan=2)
equals.grid(row=6, column=6, columnspan=2)
seven.grid(row=5, column=0, columnspan=2)
eight.grid(row=5, column=2, columnspan=2)
nine.grid(row=5, column=4, columnspan=2)
four.grid(row=4, column=0, columnspan=2)
five.grid(row=4, column=2, columnspan=2)
six.grid(row=4, column= 4, columnspan=2)
one.grid(row=3, column=0, columnspan=2)
two.grid(row=3, column=2, columnspan=2)
three.grid(row=3, column=4, columnspan=2)
divide.grid(row=2, column=0, columnspan=2)
add.grid(row=2, column=2, columnspan=2)
subtract.grid(row=2, column=4, columnspan=2)
bksp.grid(row=2, column=6, columnspan=2)
frontP.grid(row=1, column=0, columnspan=1)
backP.grid(row=1, column=1, columnspan=1)
exp.grid(row=1, column=2, columnspan=2)
multiply.grid(row=1, column=4, columnspan=2)
clr.grid(row=1, column=6, columnspan=2)
moveLeft.grid(row=3, column=6, columnspan=1)
moveRight.grid(row=3, column=7, columnspan=1)
pi.grid(row=4, column=6, columnspan=2)
squared.grid(row=5, column=6, columnspan=2)

# Main Loop
root.mainloop()
