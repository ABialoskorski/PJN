import re
file = open('N:/5.semestr/PJN/cw4/emails.html', encoding="utf-8")
data = file.read()
founded = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
                     str(data))
print(founded)
