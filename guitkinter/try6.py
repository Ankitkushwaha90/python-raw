import tkinter as tk

window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="this is calculator")
label1.grid(row=0, column=0)

nameentrya = tk.Entry(window,width=250,height=20)
nameentryb = tk.Entry(window,width=250,height=20)

nameentrya.grid(row=1,column=1)
nameentrya.grid(row=2,column=1)
window.mainloop()