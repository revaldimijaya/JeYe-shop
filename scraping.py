from bs4 import BeautifulSoup
import json

HTMLFile = open("index.html", "r")

contents = HTMLFile.read()

soup = BeautifulSoup(contents, 'html5lib')

contents = []

for attr in soup.findAll('div', attrs= {'class':'card-inner'}):
    content = {}
    content['image-location'] = attr.img['src']
    content['image-name'] = attr.img['src'].split('/')[1].split('.')[0]
    content['image-extension'] = attr.img['src'].split('/')[1].split('.')[1]
    content['title'] = attr.find('div', attrs= {'class':'card-title'}).p.text.lower()
    content['price'] = attr.find('div', attrs= {'class':'card-price'}).p.text.split(' ')[1]
    contents.append(content)

# for content in contents:
#     print(content)

with open('data.json', 'w') as f:
    json.dump(contents, f)