from tkinter import*
from PIL import *
from PIL import ImageTk, Image

window = Tk()


my = ImageTk.PhotoImage(Image.open("ankit.jpg"))

frame1 = Frame(window,width=400, height=500)
frame1.pack()

table = Label(frame1,image=my, height=100, width=100)
table.pack()

table1 = Label(table, height=100, width=100)
table1.pack()




#frame1 = tk.Frame(master=window, height=100, bg="red")
#frame1.pack(fill=tk.X)

#frame2 = tk.Frame(master=window, height=50, bg="yellow")
#frame2.pack(fill=tk.X)

#frame3 = tk.Frame(master=window, height=25, bg="blue")
#frame3.pack(fill=tk.X)

window.mainloop()