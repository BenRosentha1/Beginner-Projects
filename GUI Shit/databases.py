"""
This is a tkinter GUI that handles a database in the form of a contact book.
"""
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Import
from tkinter import *
import sqlite3
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Window Declaration
root = Tk()
root.title("contacts")
#root.iconbitmap("Location of ICO File")
root.geometry("750x450")


# Databases
connect = sqlite3.connect("contacts.db")
c = connect.cursor()

# c.execute("""CREATE TABLE contacts (
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
    connect = sqlite3.connect("contacts.db")
    c = connect.cursor()
    
    # Add values to database
    c.execute("INSERT INTO contacts VALUES (:fName, :lName, :nName, :picture, :phoneNumber, :street, :city, :state, :zipcode)",
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

    # Commit and Close
    connect.commit()
    connect.close()


def show():
    # Connect and Cursor
    connect = sqlite3.connect("contacts.db")
    c = connect.cursor()


    c.execute("SELECT *, oid FROM contacts")
    contacts = c.fetchall()

    # Build line
    result = ""
    for contact in contacts:
        result += str(str(contact[9]) + " " + str(contact[0]) + " " + str(contact[1])) + "\n"
    
    # Print
    resultLabel = Label(root, text=result)
    resultLabel.grid(row=0, column=2, columnspan=2, rowspan=10)

    # Commit and Close
    connect.commit()
    connect.close()

def delete(oid):
    # Connect and Cursor
    connect = sqlite3.connect("contacts.db")
    c = connect.cursor()
    
    c.execute(f"DELETE FROM contacts WHERE oid={oid}")
    
    # Commit and Close
    connect.commit()
    connect.close()

def editEnter():
    # Connect and Cursor
    connect = sqlite3.connect("contacts.db")
    c = connect.cursor()

    recordID = deleteBox.get()
    c.execute("""UPDATE contacts SET
        fName = :first,
        lName = :last,
        nName = :nName,
        picture = :picture,
        phoneNumber = :phoneNumber,
        street = :street,
        city = :city,  
        state = :state,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
        "fName" : fNameBoxEdit.get(),
        "lName" : lNameBoxEdit.get(),
        "nName" : nNameBoxEdit.get(),
        "picture" : pictureBoxEdit.get(),
        "phoneNumber" : phoneNumberBoxEdit.get(),
        "street" : streetBoxEdit.get(),
        "city" : cityBoxEdit.get(),  
        "state" : stateBoxEdit.get(),
        "zipcode" : zipcodeBoxEdit.get(),
        "oid" : recordID
        } )

    # Commit and Close
    connect.commit()
    connect.close()

    editW.destroy()


def edit(oid):
    # Window Declaration
    global editW
    editW = Tk()
    editW.title("Edit Window")
    #root.iconbitmap("Location of ICO File")
    editW.geometry("750x450")
    
    # Connect and Cursor
    connect = sqlite3.connect("contacts.db")
    c = connect.cursor()

    # Globalize
    global fNameBoxEdit
    global lNameBoxEdit
    global nNameBoxEdit
    global pictureBoxEdit
    global phoneNumberBoxEdit
    global streetBoxEdit
    global cityBoxEdit
    global stateBoxEdit
    global zipcodeBoxEdit

    # Text Boxes
    fNameBoxEdit = Entry(editW, width=30)
    lNameBoxEdit = Entry(editW, width=30)
    nNameBoxEdit = Entry(editW, width=30)
    pictureBoxEdit = Entry(editW, width=30)
    phoneNumberBoxEdit = Entry(editW, width=30)
    streetBoxEdit = Entry(editW, width=30)
    cityBoxEdit = Entry(editW, width=30)
    stateBoxEdit = Entry(editW, width=30)
    zipcodeBoxEdit = Entry(editW, width=30)
    c.execute(f"SELECT * FROM contacts WHERE oid = {oid}")
    contacts = c.fetchall()

    for contact in contacts:
        fNameBoxEdit.insert(0, str(contact[0]))
        lNameBoxEdit.insert(0, str(contact[1]))
        nNameBoxEdit.insert(0, str(contact[2]))
        pictureBoxEdit.insert(0, str(contact[3]))
        phoneNumberBoxEdit.insert(0, str(contact[4]))
        streetBoxEdit.insert(0, str(contact[5]))
        cityBoxEdit.insert(0, str(contact[6]))
        stateBoxEdit.insert(0, str(contact[7]))
        zipcodeBoxEdit.insert(0, str(contact[8]))

    # Labels
    fNameLabelEdit = Label(editW, text="First Name: ")
    lNameLabelEdit = Label(editW, text="Last Name: ")
    nNameLabelEdit = Label(editW, text="Nick-Name: ")
    pictureLabelEdit = Label(editW, text="Picture: ")
    phoneNumberLabelEdit = Label(editW, text="Phone Number: ")
    streetLabelEdit = Label(editW, text="Street: ")
    cityLabelEdit = Label(editW, text="City: ")
    stateLabelEdit = Label(editW, text="State: ")
    zipcodeLabelEdit = Label(editW, text="Zip Code: ")

    # Buttons
    enterBtnEdit = Button(editW, text="Enter", command=editEnter)

    # Pack it in
    fNameLabelEdit.grid(row=0, column=0)
    lNameLabelEdit.grid(row=1, column=0)
    nNameLabelEdit.grid(row=2, column=0)
    pictureLabelEdit.grid(row=3, column=0)
    phoneNumberLabelEdit.grid(row=4, column=0)
    streetLabelEdit.grid(row=5, column=0)
    cityLabelEdit.grid(row=6, column=0)
    stateLabelEdit.grid(row=7, column=0)
    zipcodeLabelEdit.grid(row=8, column=0)

    fNameBoxEdit.grid(row=0, column=1)
    lNameBoxEdit.grid(row=1, column=1)
    nNameBoxEdit.grid(row=2, column=1)
    pictureBoxEdit.grid(row=3, column=1)
    phoneNumberBoxEdit.grid(row=4, column=1)
    streetBoxEdit.grid(row=5, column=1)
    cityBoxEdit.grid(row=6, column=1)
    stateBoxEdit.grid(row=7, column=1)
    zipcodeBoxEdit.grid(row=8, column=1)

    enterBtnEdit.grid(row=9, column=0, columnspan=2, ipadx=100)



# Buttons
enterBtn = Button(root, text="Enter", command=enter)
showBtn = Button(root, text="Show contacts", command=show)

deleteBtn = Button(root, text="Delete", command=lambda : delete(deleteBox.get()))

editBtn = Button(root, text="Edit", command=lambda : edit(editBox.get()))

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

deleteBox = Entry(root, width=10)

editBox = Entry(root, width=10)


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

deleteLabel = Label(root, text="OID to Delete:")

editLabel = Label(root, text="OID to Edit:")


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
showBtn.grid(row=10, column=0, columnspan=2, ipadx=75)

deleteBox.grid(row=11, column=1, columnspan=1, ipadx=50)
deleteBtn.grid(row=12, column=1, columnspan=1, ipadx=50)
deleteLabel.grid(row=11, column= 0)

editBox.grid(row=13, column=1, columnspan=1, ipadx=50)
editBtn.grid(row=14, column=1, columnspan=1, ipadx=50)
editLabel.grid(row=13, column= 0)

# Commit and Close
connect.commit()
connect.close()


# Main Loop
root.mainloop()