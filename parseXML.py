import elementtree.ElementTree as ET
from elementtree.ElementTree import parse
from elementtree.SimpleXMLWriter import XMLWriter
import eyeD3


import sys

def run():

	x = XMLWriter("test.xml")

	musicLibrary = x.start("musicLibrary")

	x.start("song")
	x.element("id", "2")
	x.element("title", "Jigga What/Faint")
	x.element("artist", "Linkin Park/Jay Z")
	x.element("year", "2004")
	x.element("trackNumber", "3")
	x.element("totalTracks", "6")
	x.element("genre", "Rap/Nu Metal")
	x.end("song")
	x.close(musicLibrary)	

run()
"""
# build a tree structure
root = ET.Element("musicLibrary")

head = ET.SubElement(root, "head")

title = ET.SubElement(head, "title")
title.text = "Page Title"

body = ET.SubElement(root, "body")
body.set("bgcolor", "#ffffff")

body.text = "Hello, World!"

# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)
tree.write("page.xhtml")

"""
"""

w = XMLWriter(sys.stdout)
html = w.start("html")

w.start("head")
w.element("title", "my document")
w.element("meta", name="generator", value="my application 1.0")
w.end()

w.start("body")
w.element("h1", "this is a heading")
w.element("p", "this is a paragraph")

w.start("p")
w.data("this is ")
w.element("b", "bold")
w.data(" and ")
w.element("i", "italic")
w.data(".")
w.end("p")

w.close(html)
"""