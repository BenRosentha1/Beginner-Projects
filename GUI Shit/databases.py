"""
This is a tkinter GUI that handles a database.
"""
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import
from tkinter import *
import sqlite3
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Window Declaration
root = Tk()
root.title("Title")
#root.iconbitmap("Location of ICO File")
root.geometry("750x450")


# Databases
connect = sqlite3.connect("Contacts.db")
c = connect.cursor()

#c.execute("""CREATE TABLE contacts (
#        first_name text,
#        last_name text,
#        nick_name text,
#        picture blob,
#        phone_number integer,
#        street text,
#        city text,
#        state text,
#        zipcode integer
#        )""")


# Images


# Button Functionality
def enter():
    # Connect and Cursor
    connect = sqlite3.connect("Contacts.db")
    c = connect.cursor()
    
    # Add values to database
    c.execute("INSERT INTO Contacts VALUES (:fName, :lName, :nName, :picture, :phoneNumber, :street, :city, :state, :zipcode)",
              {
                  "fName" : fNameBox.get(),
                  "lName" : lNameBox.get(),
                  "nName" : nNameBox.get(),
                  "picture" : pictureBox.get(),
                  "phoneNumber" : phoneNumberBox.get(),
                  "street" : streetBox.get(),
                  "city" : cityBox.get(),  
                  "state" : stateBox.get(),
                  "zipcode" : zipcodeBox.get()
              }
    )

    # Clear boxes
    fNameBox.delete(0, END)
    lNameBox.delete(0, END)
    nNameBox.delete(0, END)
    pictureBox.delete(0, END)
    phoneNumberBox.delete(0, END)
    streetBox.delete(0, END)
    cityBox.delete(0, END)
    stateBox.delete(0, END)
    zipcodeBox.delete(0, END)


def show():
    # Connect
    c.execute("SELECT *, oid FROM contacts")
    contacts = c.fetchall()

    # Build line
    result = ""
    for contact in contacts:
        result += str(contact) + "\n"
    
    # Print
    resultLabel = Label(root, text=result)
    resultLabel.grid(row=11, column=0, columnspan=2)


# Buttons
enterBtn = Button(root, text="Enter", command=enter)
showBtn = Button(root, text="Show Contacts", command=show)


# Text Boxes
fNameBox = Entry(root, width=30)
lNameBox = Entry(root, width=30)
nNameBox = Entry(root, width=30)
pictureBox = Entry(root, width=30)
phoneNumberBox = Entry(root, width=30)
streetBox = Entry(root, width=30)
cityBox = Entry(root, width=30)
stateBox = Entry(root, width=30)
zipcodeBox = Entry(root, width=30)


# Labels
fNameLabel = Label(root, text="First Name: ")
lNameLabel = Label(root, text="Last Name: ")
nNameLabel = Label(root, text="Nick-Name: ")
pictureLabel = Label(root, text="Picture: ")
phoneNumberLabel = Label(root, text="Phone Number: ")
streetLabel = Label(root, text="Street: ")
cityLabel = Label(root, text="City: ")
stateLabel = Label(root, text="State: ")
zipcodeLabel = Label(root, text="Zip Code: ")


# Pack it in
fNameLabel.grid(row=0, column=0)
lNameLabel.grid(row=1, column=0)
nNameLabel.grid(row=2, column=0)
pictureLabel.grid(row=3, column=0)
phoneNumberLabel.grid(row=4, column=0)
streetLabel.grid(row=5, column=0)
cityLabel.grid(row=6, column=0)
stateLabel.grid(row=7, column=0)
zipcodeLabel.grid(row=8, column=0)

fNameBox.grid(row=0, column=1)
lNameBox.grid(row=1, column=1)
nNameBox.grid(row=2, column=1)
pictureBox.grid(row=3, column=1)
phoneNumberBox.grid(row=4, column=1)
streetBox.grid(row=5, column=1)
cityBox.grid(row=6, column=1)
stateBox.grid(row=7, column=1)
zipcodeBox.grid(row=8, column=1)

enterBtn.grid(row=9, column=0, columnspan=2, ipadx=100)
showBtn.grid(row=10, column=0, columnspan=2, ipadx=100)

connect.commit()
#connect.close()


# Main Loop
root.mainloop()