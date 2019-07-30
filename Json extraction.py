"""
Extracting Data from JSON

In this assignment you will write a Python program that will prompt for a URL,
read the JSON data from that URL using urllib and then parse and extract the
comment counts from the JSON data, compute the sum of the numbers in the file
and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you
the sum for your testing and the other is the actual data you need to process
for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_260991.json (Sum ends with 97)

"""


import urllib.request, urllib.parse, urllib.error
import json
import pandas as pd

js='http://py4e-data.dr-chuck.net/comments_260991.json'
url = urllib.request.urlopen(js)
data = url.read()
info = json.loads(data)
# using panda to extract list from a dictionary
x = pd.DataFrame(info)['comments'].tolist()
lst=[]
#looping over the list of dictonary and extracting counts from key count
for item in x:
    lst.append(int(item['count']))
#printing the answer
print(sum(lst))
