#sax parser
import xml.etree.ElementTree as ET
xml_data="""
<person>
<name>sai</name>
<city>hyd</city>
</person>
"""
root=ET.fromstring(xml_data)

print(root.find("name").text)
print(root.find("city").text)
