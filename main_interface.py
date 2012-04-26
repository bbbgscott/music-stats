from Tkinter import *
import tkMessageBox
import Tkconstants
import tkFileDialog
import os
import MusicStats
from MusicStats import *
import parseXML
from parseXML import *

def callback():
	print "Call from Callback"
def about():
	tkMessageBox.showinfo("About", "About Music Stat App \n------------------------ \n This app will...")
def team():
	tkMessageBox.showinfo("Team Members", "Members of Team \n-------------------- \nDrew Callan \nAaron Dalman \nBrian Scott \nMadalyn Spivey \nJordan Williams")
def version():
	tkMessageBox.showinfo("Version", "Current Version: 1.0.1")

def info(title, text):
	tkMessageBox.showinfo(title, text)

class App:
	def __init__(self, master):
		frame = Frame(master, width=600, height=400)
		frame.pack(padx=10)
		
		if os.name == 'nt':
			photo = PhotoImage(file="images\logo.gif")
		elif os.name == 'posix':
			photo = PhotoImage(file="images/logo.gif")
		lPhoto = Label(frame, image=photo)
		lPhoto.image=photo
		lPhoto.pack(side=TOP)

		
		#Label(master, text="Directory: ").grid(row=0)
		tText       = Label (frame, text="\n Music Stat App!\n").pack(side=TOP)
		#self.new    = Button(frame, text="New", padx=35, pady=2, command=self.new).pack(side=LEFT)
		self.hello  = Button(frame, text="Run", padx=30, pady=2, command=self.run).pack(side=LEFT)
		self.askdir = Button(frame, text="Select Directory", padx=10, pady=2, command=self.askdir).pack(side=LEFT)
		self.button = Button(frame, text="Quit", padx=30, pady=2, fg="red", bg="PeachPuff", command=frame.quit).pack(side=LEFT)
		bText       = Label (frame, text="\n\n").pack(side=BOTTOM)
		
		#self.warn = Button(frame, text="Warn", command=warning("Sample", "Sample Warning"))
		#self.warn.pack(side=LEFT)
		
		self.dir_opt = options = {}
		options['initialdir'] = 'C:\\'
		options['mustexist'] = False
		options['parent'] = root
		options['title'] = 'Select your music folder'

	def askdir(self):
		"""Returns a selected directoryname."""
		stats = DirWalker()
		dirName = tkFileDialog.askdirectory(**self.dir_opt)
		stats.walk(dirName, stats.cb)
		#print dirName
		return dirName		
		
		
	def run(self):
		print "\nAnalyzing Data"
		time.sleep(1)
		print "."
		time.sleep(1)
		print "."
		time.sleep(1)
		print "."
		time.sleep(1)
		print "."
		time.sleep(1)
		print "."
		top = Toplevel()
		top.title("Catagory")
		top.label1  = Label(top, text="Please Select the Statistics You Would Like to View in Graphical Form. \n", wraplength=225).pack()
		top.album   = Button(top, text="Album", width=25, height=3, command=self.album).pack()
		top.artist  = Button(top, text="Artist", width=25, height=3, command=self.artist).pack()
		top.genre   = Button(top, text="Genre", width=25, height=3, command=self.genre).pack()
		top.length  = Button(top, text="Length", width=25, height=3, command=self.length).pack()
		top.year    = Button(top, text="Year", width=25, height=3, command=self.year).pack()
		top.label2  = Label(top, text="\n").pack()
		top.button  = Button(top, text="Exit", width=25, height=3, command=top.destroy)
		top.button.pack(padx=10, pady=5)

	def album(self):
		top = Toplevel()
		top.title("Music Stats - Album")
		if os.name == 'nt':
			graph = PhotoImage(file="\project\images\graph_album.gif")
		elif os.name == 'posix':
			graph = PhotoImage(file="/project/images/graph_album.gif")
		lPhoto = Label(top, image=graph)
		lPhoto.image=graph
		lPhoto.pack(side=TOP)
		top.button = Button(top, text="Exit", command=top.destroy)
		top.button.pack()
		
	def artist(self):
		top = Toplevel()
		top.title("Music Stats - Artist/Band")
		if os.name == 'nt':
			graph = PhotoImage(file="\project\images\graph_artist.gif")
		elif os.name == 'posix':
			graph = PhotoImage(file="/project/images/graph_artist.gif")
		lPhoto = Label(top, image=graph)
		lPhoto.image=graph
		lPhoto.pack(side=TOP)
		top.button = Button(top, text="Exit", command=top.destroy)
		top.button.pack()			
		
	def genre(self):
		top = Toplevel()
		top.title("Music Stats - Musical Genre")
		if os.name == 'nt':
			graph = PhotoImage(file="\project\images\graph_genre.gif")
		elif os.name == 'posix':
			graph = PhotoImage(file="/project/images/graph_genre.gif")
		lPhoto = Label(top, image=graph)
		lPhoto.image=graph
		lPhoto.pack(side=TOP)
		top.button = Button(top, text="Exit", command=top.destroy)
		top.button.pack()
		
	def length(self):
		top = Toplevel()
		top.title("Music Stats - Length of Songs")
		if os.name == 'nt':
			graph = PhotoImage(file="\project\images\graph_length.gif")
		elif os.name == 'posix':
			graph = PhotoImage(file="/project/images/graph_length.gif")
		lPhoto = Label(top, image=graph)
		lPhoto.image=graph
		lPhoto.pack(side=TOP)
		top.button = Button(top, text="Exit", command=top.destroy)
		top.button.pack()	

	def year(self):
		top = Toplevel()
		top.title("Music Stats - Year Released")
		if os.name == 'nt':
			graph = PhotoImage(file="\project\images\graph_year.gif")
		elif os.name == 'posix':
			graph = PhotoImage(file="/project/images/graph_year.gif")
		lPhoto = Label(top, image=graph)
		lPhoto.image=graph
		lPhoto.pack(side=TOP)
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
helpmenu.add_command(label="About...", command=about)
helpmenu.add_command(label="Team...", command=team)
helpmenu.add_command(label="Version...", command=version)

root.mainloop()