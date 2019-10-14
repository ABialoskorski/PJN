import re

file2 = 'ssa165161dafaf,5464,65464'
a = re.match('^(\w)+[,][0-9]+[,][0-9]+$', file2)

if a:
    print('dopasowano')
else:
    print('nie dopasowano')