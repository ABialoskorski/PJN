import re


with open('page.txt') as file:
    for line in file:
        line = line.rstrip()
        if re.match(r'^[a-z0-9_.-]+@[a-z0-9_.-]+\.\w{2,4}$', line):
            print(line)
