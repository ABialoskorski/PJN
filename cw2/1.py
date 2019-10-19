import re

name = 'Artur'
surname = 'Bialoskorski'
tel = '(61) 111-45-55'
zipCode = '11-123'
city = 'Poznań'

m = re.match('^[A-Z]{1}(\w)+$', name)
n = re.match('^[A-Z]{1}(\w)+$', surname)
o = re.match('^[(][0-9]{1,2}[)][ ][-\s\.0-9]*$', tel)
p = re.match('^[0-9]{2}[-][0-9]{3}$', zipCode)
q = re.match('^[A-Z]{1}(\w)+$', city)

if m and n and o and p and q:
    print('dopasowano')
else:
    print('nie dopasowano')