from bs4 import BeautifulSoup
xml_data="""
<bookstore>
<book category="cooking">
<title>Indian food</title>
<author>sss</author>
<year>2025</year>
<price>120</price>
</book>
<book category="stories">
<title>lion the kingdom</title>
<author>herry</author>
<year>2010</year>
<price>500</price>
</book>
</bookstore>"""
soup=BeautifulSoup(xml_data,"html.parser")
print("parsing using html parser")
books=soup.find_all('book')
for book in books:
    title=book.find('title').text
    author=book.find('author').text
    year=book.find('year').text
    price=book.find('price').text
    category=book.find('category')
    print(f"category:{category}")
    print(f"title:{title}")
    print(f"Author:{author}")
    print(f"year:{year}")
    print(f"price:{price}")
