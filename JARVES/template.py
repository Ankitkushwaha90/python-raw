import tkinter as tk

  
window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)


#label = tk.Label(text = "welcome to inthis page.",bg="black",fg="white")
#label.grid()

'''def click():
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2, bg="black")

    label = tk.Label(text = "welcome to inthis page.",bg="black",fg="white")
    label.grid(row=0, column=0)
     
    fr_buttons.grid(row=0, column=0, sticky="ns")'''
    
    
    # Swap the order of `frame_a` and `frame_b`

'''def back():
    label = tk.Label(text = "welcome to inthis page.",height=100, weight=50 ,bg="black",fg="white")
    label.grid()'''
    

btn_open = tk.Button(fr_buttons, text="Open", command=click)
#btn_save = tk.Button(fr_buttons, text="Save As...")


btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
#btn_save.grid(row=1, column=0, sticky="ew", padx=5)



fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()