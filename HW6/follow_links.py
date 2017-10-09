import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

position = int(input('Enter position: '))
count = int(input('Enter count: '))

for name in range(count):
    tags = soup('a')
    tags = list(tags)
    url = tags[position - 1].get('href', None)
    print (tags[position - 1].contents[0])
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')


# Grab first url, position, and count
# Go to first url
# Loop count times
# Grab link in position position
# Go to that new link
