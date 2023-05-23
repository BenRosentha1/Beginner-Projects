"""
This is a test
"""
#-----------------------------------------------------------------------
from tkinter import *
#-----------------------------------------------------------------------

# Window Declaration
root = Tk(className="Ben's Window")

# Button Functionality
def myClick():
    myClick = Label(root, text="!!!Poop Alert!!!").pack()
    searchBox = Label(root, text="Input: " + search.get()).pack()


# Labels
myLabel = Label(root, text="Hello Ben!")
myLabel2 = Label(root, text="I hope you are having a wonderful day!")
# Buttons
myButton = Button(root, text="Do Not Press!", padx=100, pady=100, command=myClick, fg="white", bg="red")
search = Entry(root, fg="black", bg="light blue", width=25, borderwidth=5)

# Pack it in
myLabel.pack()
myLabel2.pack()
search.pack()
search.insert(0, "Fuck you!")
myButton.pack()

root.mainloop()