"""
This is a template for writing programs using tinkter.
"""
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import
from tkinter import *
from PIL import ImageTk,Image
from os import *
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Window Declaration
root = Tk()
root.title("Always Sunny Best Hits!")
#root.iconbitmap("Location of ICO File")

# Images
feelings = ImageTk.PhotoImage(Image.open(r"C:\Users\benmr\OneDrive\Documents\GitHub\Beginner-Projects\GUI Shit\Image Viewer\images\Feelings.jpg").resize((400, 400)))
magnets = ImageTk.PhotoImage(Image.open(r"C:\Users\benmr\OneDrive\Documents\GitHub\Beginner-Projects\GUI Shit\Image Viewer\images\Magnets.jpg").resize((400, 700)))
pepeSilva = ImageTk.PhotoImage(Image.open(r"C:\Users\benmr\OneDrive\Documents\GitHub\Beginner-Projects\GUI Shit\Image Viewer\images\Pepe Silva.jpg").resize((400, 400)))
therapy = ImageTk.PhotoImage(Image.open(r"C:\Users\benmr\OneDrive\Documents\GitHub\Beginner-Projects\GUI Shit\Image Viewer\images\ThroughGodAllThingsArePossible.jpg").resize((400, 400)))
tribal = ImageTk.PhotoImage(Image.open(r"C:\Users\benmr\OneDrive\Documents\GitHub\Beginner-Projects\GUI Shit\Image Viewer\images\Tribal.jpg").resize((400, 400)))
images = [feelings, magnets, pepeSilva, therapy, tribal]

# Button Functionality
def forward(num):
    global pic
    global forwardBtn
    global backBtn

    pic.grid_forget()
    pic = Label(image=images[num+1])
    pic.grid(row=0, column=0, columnspan=3)
    forwardBtn = Button(root, text=">>", command=lambda:forward(num), padx=50, pady=50)
    backBtn = Button(root, text="<<", command=lambda:back(num-1), padx=50, pady=50)

def back():
    global pic
    global forwardBtn
    global backBtn

    pic.grid_forget()
    pic = Label(image=images[num+1])
    pic.grid(row=0, column=0, columnspan=3)
    forwardBtn = Button(root, text=">>", command=lambda:forward(2))
    backBtn = Button(root, text="<<", command=lambda:back(num-1))


# Buttons
forwardBtn = Button(root, text=">>", command=lambda: forward(1))
backBtn = Button(root, text="<<", command=lambda: back(0))

# Labels
pic = Label(image=images[0])

# Pack it in
pic.grid(row=0, column=0, columnspan=2)
backBtn.grid(row=1, column=0, columnspan=1)
forwardBtn.grid(row=1, column=1, columnspan=1)

# Main Loop
root.mainloop()
