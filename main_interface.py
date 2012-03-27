from Tkinter import *
import tkMessageBox

def callback():
	print "called the callback"

def warning(title, text):
	tkMessageBox.showwarning(title, text)

class App:
	def __init__(self, master):
		frame = Frame(master, width=600, height=400)
		frame.pack()

		#Label(master, text="Directory: ").grid(row=0)

		self.button = Button(frame, text="Quit", fg="red", bg="PeachPuff", command=frame.quit)
		self.button.pack(side=LEFT)

		self.hello = Button(frame, text="Hello", command=self.hi)
		self.hello.pack(side=LEFT)

		self.new = Button(frame, text="New", command=self.new)
		self.new.pack(side=LEFT)

		#self.warn = Button(frame, text="Warn", command=warning("Sample", "Sample Warning"))
		#self.warn.pack(side=LEFT)

	def hi(self):
		print "Hello, World"

	def new(self):
		top = Toplevel()
		top.title("Popup")
		top.button = Button(top, text="Exit", command=top.destroy)
		top.button.pack()

root = Tk()

app = App(root)

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=callback)
filemenu.add_command(label="Open...", command=callback)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=callback)

root.mainloop()