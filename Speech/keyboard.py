from tkinter import *
import pyautogui
import tkinter.messagebox
from sp2txt import microphone

root = Tk()
root.title("Abler")
root.geometry("500x250+"+str(root.winfo_screenwidth()-500)+"+"+str(root.winfo_screenheight()-250))
name = Label(root, text="Event Viewer : ")
entry = Entry(root)
Text = StringVar()


def Button1(event):
	global Text
	Text.set('Event Viewer : Recording button pressed!')
	entry.delete(0, 'end')
	microphone()


def Button2(event):
	global Text
	pyautogui.press("capslock")
	Text.set('Event Viewer : Capslocks pressed!')


def Button3(event):
	global Text
	Text.set('Event Viewer : Quit button pressed!')
	ans = tkinter.messagebox.askokcancel('Confirm Exit', 'Are you sure want to exit?')
	if ans:
		quit()


def GUI():

	Text.set("Event Viewer : ")
	name = Label(root, textvariable=Text)
	button1 = Button(root, text="Turn ON microphone", height=10, width=15)
	button2 = Button(root, text="CapsLocks", height=10, width=15)
	button3 = Button(root, text="Quit", height=10, width=15)
	name.grid(row=0, column=0, sticky=W, columnspan=3)
	entry.grid(row=1, column=0)
	button1.grid(row=2, column=0)
	button2.grid(row=2, column=1)
	button3.grid(row=2, column=2)
	button1.bind("<Button-1>", Button1)
	button2.bind("<Button-1>", Button2)
	button3.bind("<Button-1>", Button3)
	root.mainloop()
GUI()