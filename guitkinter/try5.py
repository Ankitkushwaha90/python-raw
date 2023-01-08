
from tkinter import *

root = Tk()

def sum():
	
	namevaluea = a
	namevalueb = b
	calculators = a + b
	print(calculators)
	


root.geometry("644x344")
#Heading
Label(root, text="calculator", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)


# Tkinter variable for storing entries
namevaluea = StringVar()
namevalueb = StringVar()
namevaluec = StringVar()


#Entries for our form
nameentry = Entry(root, textvariable=namevaluea)
phoneentry = Entry(root, textvariable=namevalueb)
phoneentry = Entry(root, textvariable=namevaluec)

# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
phoneentry.grid(row=3, column=3)


#Button & packing it and assigning it a command
Button(text="Sum" ,command=sum).grid(row=7, column=3)



root.mainloop()
