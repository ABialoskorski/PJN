import requests
from bs4 import BeautifulSoup
import urllib.request

def crawler():
    url = 'http://rjawor.home.amu.edu.pl/'
    html = requests.get(url)
    text = html.text
    soup = BeautifulSoup(text, "html.parser")
    for link in soup.findAll('a'):
        href = link.get('href')
        if href[-4:] == '.php':
            href = 'http://rjawor.home.amu.edu.pl/' + href
        if href[:7] == 'mailto:':
            continue
        single_page(href)
def single_page(url):
    response = urllib.request.urlopen(url)
    page = response.read().decode('utf-8')
    pf = BeautifulSoup(page, "html.parser").get_text()
    all += pf

crawler()
print(all)
