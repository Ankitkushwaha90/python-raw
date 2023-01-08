import tkinter as tk

def function():	
	c=x
	b=y
	a=b+c
	print(a)



window= tk.Tk()



window.geometry("300x300")
window.title("new window")



txt=tk.Entry(window, width=20)
txt.grid(row=0,column=3)

txt=tk.Entry(window, width=20)
txt.grid(row=2,column=3)

btn = tk.Button(window, text="sum", fg="yellow")
btn.grid(row=3,column=30)


window.mainloop()