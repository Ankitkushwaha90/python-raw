from tkinter import*


window = Tk()

def sum(calculator):
	
	namevaluea = a
	namevalueb = b
	calculators = a + b


label_a = Label(window, text="this is calculator",width=250,height=20)
label_a.pack()

#nameentrya = IntVar()
#nameentryb = IntVar()

nameentrya = Entry(window,width=250,height=20)
nameentryb = Entry(window,width=250,height=20)

nameentrya.pack()
nameentrya.pack()

btn=Button(text="Sum", command=sum,width=250,height=20)
btn.pack()




window.mainloop()