import urllib.request
import re
from bs4 import BeautifulSoup

html = urllib.request.urlopen(
    "https://www.ceneo.pl/Szlifierki_i_polerki/Rodzaj:Szlifierki_katowe;0020-30-0-0-2.htm")

html = html.read().decode('utf-8')
szliferki = re.findall(
        r'<a href="/[0-9]+"   data-reviewshref="" class="go-to-product js_conv js_clickHash js_seoUrl" data-source-tag=""> [A-Za-z0-9-( )]+</a>', str(html))

szliferki = BeautifulSoup(str(szliferki), "html.parser").text
print(szliferki)
