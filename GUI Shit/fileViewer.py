"""
This is a file viewer that implements tkinters functionality to create a GUI.
"""
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import
from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Window Declaration
root = Tk()
root.title("File Viewer")
#root.iconbitmap("")


# Files
root.filename = fd.askopenfilename(initialdir=r"C:\\Users\benmr\\OneDrive\\Documents\\GitHub\\Beginner-Projects\\GUI Shit\\Image Viewer\\images", title="Select a File", filetypes=(("png files", "*.png"), ("all", "*.*")))
imagePath = Label(root, text=root.filename).pack()
image = ImageTk.PhotoImage(Image.open(root.filename))
imageLabel = Label(image=image).pack()

# Methods


# Labels


# Buttons


# Main Loop
root.mainloop()
