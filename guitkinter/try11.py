
from tkinter import *

root = Tk()


def cal(x,y):
	a=b+c
	b=int(namevalue)
	c=int(phonevalue)
	print(a)


   
root.geometry("644x344")
#Heading
Label(root, text="Welcome to Harry Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
name = Label(root, text="Name")
phone = Label(root, text="Phone")

#Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)

# Tkinter variable for storing entries
'''
namevalue = StringVar()
phonevalue = StringVar()
'''


#Entries for our form
nameentry = Entry(root, textvariable=int(namevalue))
phoneentry = Entry(root, textvariable=int(phonevalue))

# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)


#Button & packing it and assigning it a command
Button(text="Submit to Harry Travels",command=cal(namevalue,phonevalue)).grid(row=7, column=3)



root.mainloop()
