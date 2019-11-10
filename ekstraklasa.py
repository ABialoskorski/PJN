import re
import urllib.request
from bs4 import BeautifulSoup

clubs = []

for n in range(2019, 2008, -1):
    response = urllib.request.urlopen("https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_({0}/{1})".format(n-1, n))
    html = response.read() .decode('utf-8')
    clubs += re.findall(r'<td align="left"><a href="\/wiki\/[^"]+" title="[^"\d]+">([^"\d<]+ [^"\d<]+|Cracovia)<\/a>[^<]', str(html))
clubs = list(set(clubs))

wszystko = {}

for elem in clubs:
    if elem != "Termalica Bruk-Bet Nieciecza":
        wszystko[elem] = 0

for n in range(2019, 2008, -1):
    response = urllib.request.urlopen("https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_({0}/{1})".format(n-1, n))
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    if n < 2014:
        soup = soup.find(id="Tabela").parent
    else:
        soup = soup.find(id="Tabela_2").parent

    tabela_wynikow = soup.next_sibling.next_sibling

    for elTabeli in tabela_wynikow.find_all('a'):
        name = re.findall(r'<a href="\/wiki\/[^"]+" title="[^"\d]+">([^"\d<]+ [^"\d<]+|Cracovia)<\/a>', str(elTabeli))

        if len(name) > 0:
            if name[0] == "Termalica Bruk-Bet Nieciecza":
                name[0] = "Bruk-Bet Termalica Nieciecza"
            if name[0] in clubs:
                wyniki = elTabeli.parent
                for el in range(16):
                    wyniki = wyniki.next_sibling
                wyniki = wyniki.next
                punkty = re.findall(r'<b>(\d+)<\/b>', str(wyniki))
                wszystko[name[0]] += int(punkty[0])

print(wszystko)
