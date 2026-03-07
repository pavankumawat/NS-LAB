from html.parser import HTMLParser

class Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Tag: {tag}")
    
    def handle_data(self, data):
        if data.strip():
            print(f"Data: {data}")

xml = """
<students>
  <student>
    <name>John</name>
    <age>20</age>
  </student>
  <student>
    <name>Sara</name>
    <age>19</age>
  </student>
</students>
"""

parser = Parser()
parser.feed(xml)