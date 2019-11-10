import urllib.request
import re
from bs4 import BeautifulSoup
from subprocess import call
import nltk
from nltk import word_tokenize,sent_tokenize


nltk.download('punkt')


response = urllib.request.urlopen(
    "http://rjawor.home.amu.edu.pl/index.php")
page_pl_1 = response.read().decode('utf-8')
pl_1 = BeautifulSoup(page_pl_1, "html.parser").get_text()

response = urllib.request.urlopen(
    "http://rjawor.home.amu.edu.pl/education.php")
page_pl_2 = response.read().decode('utf-8')
pl_2 = BeautifulSoup(page_pl_2, "html.parser").get_text()

response = urllib.request.urlopen(
    "http://rjawor.home.amu.edu.pl/science.php")
page_pl_3 = response.read().decode('utf-8')
pl_3 = BeautifulSoup(page_pl_3, "html.parser").get_text()

response = urllib.request.urlopen(
    "http://rjawor.home.amu.edu.pl/relax.php")
page_pl_4 = response.read().decode('utf-8')
pl_4 = BeautifulSoup(page_pl_4, "html.parser").get_text()

response = urllib.request.urlopen(
    "http://rjawor.home.amu.edu.pl/contact.php")
page_pl_5 = response.read().decode('utf-8')
pl_5 = BeautifulSoup(page_pl_5, "html.parser").get_text()

response = urllib.request.urlopen(
    "http://rjawor.home.amu.edu.pl/index_en.php")
page_eng_1 = response.read().decode('utf-8')
eng_1 = BeautifulSoup(page_eng_1, "html.parser").get_text()

response = urllib.request.urlopen(
    "http://rjawor.home.amu.edu.pl/education_en.php")
page_eng_2 = response.read().decode('utf-8')
eng_2 = BeautifulSoup(page_eng_2, "html.parser").get_text()

response = urllib.request.urlopen(
    "http://rjawor.home.amu.edu.pl/science_en.php")
page_eng_3 = response.read().decode('utf-8')
eng_3 = BeautifulSoup(page_eng_3, "html.parser").get_text()

response = urllib.request.urlopen(
    "http://rjawor.home.amu.edu.pl/relax_en.php")
page_eng_4 = response.read().decode('utf-8')
eng_4 = BeautifulSoup(page_eng_4, "html.parser").get_text()

response = urllib.request.urlopen(
    "http://rjawor.home.amu.edu.pl/contact_en.php")
page_eng_5 = response.read().decode('utf-8')
eng_5 = BeautifulSoup(page_eng_5, "html.parser").get_text()

pages_pl = pl_1 + pl_2 + pl_3 + pl_4 + pl_5
pages_eng = eng_1 + eng_2 + eng_3 + eng_4 + eng_5

pagesPL = re.sub(
    r'(\n|\t)+', '.', pages_pl)
pagesPL = sent_tokenize(pagesPL, language="polish")

with open('C:/Users/WHITE SKIN/Desktop/pjn/polish.txt', 'w', encoding='utf-8') as file:
    for item in pagesPL:
        file.write("%s\n" % item)

pagesENG = re.sub(
    r'(\n|\t)+', '.', pages_eng)
pagesENG = sent_tokenize(pagesENG, language="english")

with open('C:/Users/WHITE SKIN/Desktop/pjn/english.txt', 'w', encoding='utf-8') as file:
    for item in pagesENG:
        file.write("%s\n" % item)

call('LF_aligner_3.1.exe --filetype="t" --infiles="C:/Users/WHITE SKIN/Desktop/pjn/english.txt","C:/Users/WHITE SKIN/Desktop/pjn/polish.txt" --languages="en","pl" --segment="y" --review="n" --tmx="n"')
