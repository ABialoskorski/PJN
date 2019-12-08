import urllib.request
from bs4 import BeautifulSoup
import re

titles = []

for x in range(1,30):
  with urllib.request.urlopen("https://www.narzedzia.pl/katowe,c12395,{}/?gclid=EAIaIQobChMI_6yfldfM3gIVFuWaCh1reg_SEAAYASAAEgLRx_D_BwE".format(str(x))) as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    pattern = re.compile(r"szlifierka kątowa (.*)",re.IGNORECASE)
    for a in soup.find_all("a"):
      if a.string:
        word = pattern.search(a.string)
        if word:
          word = word.group(1)
          print(word)
          titles.append(word)
print("----------------------WYNIKI----------------------------")
lista = list(set(titles))
lista = filter(lambda x: not re.search(r"^[0-9]+ mm|^\+.*",x),lista)
for e in sorted(lista):
  print(e)
