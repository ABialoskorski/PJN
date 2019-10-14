import re
#re.findall - wyszuka wszystkie wystapienia wzorca
name = 'Artur'
surname = 'Bialoskorski'
tel = '(61) 213-45-55'
zipCode = '11-123'
city = 'Poznań'

m = re.match('^[A-Z]{1}[a-z]+$', name)
n = re.match('^[A-Z]{1}[a-z]+$', surname)
o = re.match('^[(][0-9]{1,2}[)][ ][-\s\.0-9]*$', tel)
p = re.match('^[0-9]{2}[-][0-9]{3}$', zipCode)
q = re.match('^[A-Z]{1}[a-z]+$', city)

if m and n and o and p and q:
    print('dopasowano')
else:
    print('nie dopasowano')

with open('sciezka') as in_file:
    for line in in_file:
        print(line.strip())