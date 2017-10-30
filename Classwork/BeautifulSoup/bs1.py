import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
with open("index.html") as fp:
    soup = BeautifulSoup(fp, "lxml")
tags = soup('a')
for tag in tags:
	print(tag.get('href', None))

#Kinds of objects
#Tags
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', "lxml")
tag = soup.b
print(type(tag))

#Names
tag.Names
tag.name = "blockquote"
print(tag)

#Attributes
tag['id']

tag.attrs

tag['id'] = 'verybold'
tag['another-attribute'] = 1
tag
