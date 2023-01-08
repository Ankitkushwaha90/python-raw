from tkinter import *



root=Tk()
root.geometry('500x300')
root.title('speaking')


import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()





def catch():
	d=btn1.get()
	speak(d)
	print("hello")


def whello():
	def canc():
		cancle=10>9
	a=1
	
	while a<5:
		
		d=btn1.get()
		speak(d)
		print("hello")
		a+=1

def canc():
	cancle=10>9
	print("who are you")
	
btn1=Entry(root)
btn1.grid(row=1,column=2,padx=5,pady=5)


btn=Button(root, text="speak",command=catch)
btn.grid(row=1,column=1,padx=5,pady=5)


btn3=Button(root, text="whileloop", command=whello)
btn3.grid(row=2,column=1,padx=0,pady=0)


btn4=Button(root, text="cancle", command=canc)
btn4.grid(row=2,column=2,padx=0,pady=0)



root.mainloop()