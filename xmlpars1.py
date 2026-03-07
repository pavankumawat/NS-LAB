#sax parser 
import xml.etree.ElementTree as ET

tree=ET.parse("lib.xml")
root=tree.getroot()
for book in root:
    title=book.find("title").text
    author=book.find("author").text
    print(title,author)
    
