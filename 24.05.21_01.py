from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.tilte.string)
# print(soup.prettify())
# print(soup.a)

all_anchor_tags = soup.find_all(name="a")
#print(all_anchor_tags)
for tag in all_anchor_tags:
  #print(tag.getText())
   print(tag.get("href"))

heading = soup.find(name="h1", id="name")
#rint(heading)
section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get("class"))