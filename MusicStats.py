import os
import sys
import eyeD3
import xml.sax.handler
import re

# Thanks to http://ssscripting.wordpress.com/2009/03/03/python-recursive-directory-walker/
class DirWalker(object):
	def walk(self, dir, meth):
		""" walks a directory and executes a callback on each file """
		dir = os.path.abspath(dir)
		for file in [file for file in os.listdir(dir) if not file in [".", ".."]]:
			nfile = os.path.join(dir, file)
			if os.path.isdir(nfile):
				print "Here First"
				self.walk(nfile, meth)
			else:				
				meth(nfile)

	def cb(self, file):
		allowedList = [".mp3"]
		ext = os.path.splitext(file)
		tag = eyeD3.Tag()
		tag.link(file)
		#print ext[1]
		if os.path.splitext(file)[1] in allowedList:
			print os.path.splitext(file)[0] + ext[1]
			print "Artist: %s" % tag.getArtist()
			print "Album: %s" % tag.getAlbum()
			print "Title: %s" % tag.getTitle()
			print "Year: %s" % tag.getYear()
			print "Track#: %s" % tag.getTrackNum()[0]
			g = str(tag.getGenre())
			m = re.search('(?<=\\))\w+', g)
			print "Genre: %s" % str(m.group(0))
			print ' '

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