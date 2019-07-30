import re
def getNumbers(str):
    number = re.findall(r'[0-9]+', str)
    return number
str= open('regex_sum_260986.txt',"r").read()
array= getNumbers(str)

desired_array = [int(numeric_string) for numeric_string in array]
sumno=sum(desired_array)
print(sumno)
pip install beautifulsoup4
