import re

file4 = open('page.html')
data = file4.read()
maile = re.findall(r'[a-zA-Z0-9_.+]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+',
    str(data))

print(maile)
