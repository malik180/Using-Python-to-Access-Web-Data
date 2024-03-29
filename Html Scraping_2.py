"""
In this assignment you will write a Python program that expands on
http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the
HTML from the data files below, extract the href= vaues from the anchor tags,
scan for a tag that is in a particular position relative to the first name in
the list, follow that link and repeat the process a number of times and report
the last name you find.

We provide two files for this assignment. One is a sample file where we give you
the name for your testing and the other is the actual data you need to process
for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this
 process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Ari.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this
process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: A
"""

# Retrieve all of the anchor tags
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
position=18
url='http://py4e-data.dr-chuck.net/known_by_Ari.html'
for x in range(7):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    list=[]
    for tag in tags:
        list.append(tag.get('href', None))
    url=list[position-1]
print(url)
