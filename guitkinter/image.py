from tkinter import * 
from PIL import *
from PIL import ImageTk, Image

#window = tk.Tk()
#window.columnconfigure(0, minsize=250)
#window.rowconfigure([0, 1], minsize=100)
root =Tk()



root.title('ankit kushwaha')


root.geometry("1000x500")

my = ImageTk.PhotoImage(Image.open("ankit.jpg"))

frame= Frame(root,width=900,height=500)
frame.grid()

img = Label(frame,image=my, text="ankit kushwaha",width=900,height=500)
img.grid(row=0,column=0)


#text= Label( text="ankit kushwaha",fg="black")
#text.pack(side="left")

def hello():
    print("Hello tkinter Buttons")

def name():
    print("Name is harry")


b1 = Button(frame, fg="red", text="Print now", command=hello)
b1.grid(row=0, column=0,pady=3,padx=20,sticky="w" )

b2 = Button(frame, fg="red", text="Tell me name now", command=name)
b2.grid(row=0,column=0,pady=300,padx=200,sticky="wn")

b3 = Button(frame, fg="red", text="Print now")
b3.grid(row=0,column=0,ipady=15,ipadx=7,sticky="w")

b4 = Button(frame, fg="red", text="Print now")
b4.grid(row=0,column=0,ipady=22,ipadx=18,sticky="w")

root.mainloop()