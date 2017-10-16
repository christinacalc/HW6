# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url_list= []
url = input('Enter - ')
n= 0

while n < 7:
	lst_of_tags= []
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')

	for i in range(8):
		for each in tags:
			lst_of_tags.append(each)	

	url= lst_of_tags[17].get('href', None)
	url_list.append(url)

	n= n+1

end= re.findall('by_([^ ]*).html', url)
print("The answer is: " + end[0])