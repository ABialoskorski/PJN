#linie składające się z trzech pól, z czego pierwsze pole jest dowolnym łańcuchem
#znaków, a drugie i trzecie - liczbą całkowitą. Separatorem jest znak średnika.
# -*- coding: utf-8 -*-
import re
with open('N:/5.semestr/PJN/cw2/test.csv') as in_file:
    for line in in_file:
        if not (re.match(r"[^;]+;\d+;\d+", line)):
            print("uncorrect format data")
            break
