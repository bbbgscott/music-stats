import elementtree.ElementTree as ET
from elementtree.SimpleXMLWriter import XMLWriter
import os.path

import sys

def run1():
	x = XMLWriter("test.xml")

	musicLibrary = x.start("musciLibrary")

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

run1()

def run2():
	# Create root
	root = xml.Element('root')

	#Create a child element
	child = xml.Element('child')
	root.append(child)

	#Set element attributes
	child.attrib['artist'] = " artist name goes here"
	child.attrib['album'] = "album name goes here"
	child.attrib['title'] = "title goes here"
	child.attrib['year'] = "year goes here"
	child.attrib['track'] = "track goes here"
	child.attrib['genre'] = "genre goes here"

	#Write to an .xml file on the hard drive

	#Open a file
	file = open("c:/library.xml", 'w')

	#Create an ElementTree object from the root element
	xml.ElementTree(root).write(file)

	#Close the file
	file.close()

	// insert

	#Parse XML directly from the file path
	tree = xml.parse("c:/library.xml")

	#Get the root node
	rootElement = tree.getroot()

	#Get a list of children elements with tag == "library"
	libraryList = rootElem.findall("library")

	#Check if any "songs" were found

	      

	# Set up XML text writer

	XmlTextWriter xtw = new XmlTextWriter("Test.xml", System.Text.Encoding.UTF8);
	xtw.Formatting = Formatting.Indented;
	xtw.Indentation = 3;
	xtw.IndentChar = ' ';
	xtw.WriteStartDocument(true);
	xtw.WriteStartElement("root");
	for (int i = 0; i < 500000; i++)
	  xtw.WriteElementString("child", "This is child number " + i.ToString());
	xtw.WriteEndElement();
	xtw.WriteEndDocument();
	xtw.Close();

	#append rows

	XmlDocument doc = new XmlDocument();
	doc.Load("library.xml");
	XmlElement el = doc.CreateElement("child");
	el.InnerText = "This row is being appended to the end of the document.";
	doc.DocumentElement.AppendChild(el);
	doc.Save("library.xml");