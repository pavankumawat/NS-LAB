#DOM parser
from xml.dom import minidom
doc=minidom.parse("sample.xml")
root=doc.documentElement
print("Root element",root.tagName)
students=doc.getElementsByTagName("student")
for student in students:
    name=student.getElementsByTagName("name")[0].firstChild.nodeValue
    age=student.getElementsByTagName("age")[0].firstChild.nodeValue
    print("Name:",name,"Age:",age)
