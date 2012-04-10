import os
import sys
import eyeD3
import xml.sax.handler

# Thanks to http://ssscripting.wordpress.com/2009/03/03/python-recursive-directory-walker/
class DirWalker(object):
	def walk(self, dir, meth):
		""" walks a directory and executes a callback on each file """
		dir = os.path.abspath(dir)
		for file in [file for file in os.listdir(dir) if not file in [".", ".."]]:
			nfile = os.path.join(dir, file)
			meth(nfile)
			if os.path.isdir(nfile):
				self.walk(nfile, meth)

	def cb(self, file):
		allowedList = [".wav", ".aif", ".mp3", ".mid", ".ogg", ".m4a", ".mpa", ".wma"]
		ext = os.path.splitext(file)
		#print ext[1]
		if os.path.splitext(file)[1] in allowedList:
			print os.path.splitext(file)[0] + ext[1]

def stripPath(file):
	if file.partition('\\')[2]:
		stripPath(file.partition('\\')[2])
	else:
		print file
"""
pth = raw_input("Please enter a path: ")
print pth
DirWalker().walk(pth, cb)
"""