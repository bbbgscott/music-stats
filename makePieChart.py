#!/usr/bin/python

import cairo
#import Pycairo
import cairoplot
import elementtree.ElementTree as ET
from elementtree.ElementTree import parse
import xml.etree.ElementTree as xml
import collections
from PIL import Image, ImageSequence, ImagePalette

genre = []
year = []
length = []

tree = xml.parse("c:/project/list.xml")
rootElement = tree.getroot()
songList = rootElement.findall("SONG")

if songList != None:
	for song in songList:
		gkey = song.findtext("GENRE")
		genre.append(gkey)
		ykey = song.findtext("YEAR")
		year.append(ykey)
		lkey = song.findtext("LENGTH")
		length.append(lkey)
		


def chartGenre():	
	genre.sort()
	c = collections.Counter(genre)
	cairoplot.pie_plot('C:\project\images\pie_genre.png', c, 480, 640, background = None, gradient = False, shadow = False, colors=None)
	im = Image.open("C:\project\images\pie_genre.png")
	im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE)
	im.save('C:\project\images\pie_genre.gif')	
	print "Created Genre Pie Chart"



chartGenre()



























# import pylab
# from pylab import *
# 
	
# def chartYear():	
	# figure(3, figsize=(4,4))
	# axes([0.1, 0.1, 0.8, 0.8])

	# mcolors=['blue', 'brown', 'red', 'green', 'yellow', 'orange']
	# mlabels=['1960s', '1970s', '1980s', '1990s', '2000s', '2010s']
	# fracs=[16, 5, 10, 21, 6, 2]
	# pie(fracs, labels=mlabels, colors=mcolors)

	# savefig('C:\project\images\pie_year.png')

	# ima = Image.open("C:\project\images\pie_year.png")
	# ima = ima.convert('RGB').convert('P', palette=Image.ADAPTIVE)
	# ima.save('C:\project\images\pie_year.gif')
	# print "Created Year Chart"
		
# chartGenre()		
# chartYear()