import re

with open(
        'przeklenstwa.txt') as in_file:
    plik3 = in_file.read()
    changes = re.sub(
        r"([a-zA-ZżźćńółęąśŻŹĆĄŚĘŁÓŃ]*)((obsr(y|a|w))+|((kur(w|ew|est))+|(dup(a|e|y|i|c))+|(szmato)+|(kurwa)|"
        r"(fiu(t|c))+|(jeb(a|i|c|m|n|l|))+|(kuta(s|f))+|(pi(z|ź)d)+|(downi)+|(sperm)+|(chuj)+|"
        r"(mord(a|e))|(debil)|(zapier)+|(rucha)+|(cip)+|(dziwk)))([a-zA-ZżźćńółęąśŻŹĆĄŚĘŁÓŃ]*)",
        "---", plik3)
file = open(
    'po_zmianie.txt', "a")
file.write(changes)
