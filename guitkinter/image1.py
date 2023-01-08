from tkinter import *
window = Tk()
window.title('Grand Canyon')
canvas = Canvas(window, width =500, height=500)
canvas.pack()
my_image = PhotoImage(file ='C:\\guitkinter\\ankit.jpg')
canvas.create_image(my_image)
