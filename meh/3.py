import re
with open(
        'N:/5.semestr/PJN/cw3/wulgarneslowa.txt', encoding="utf-8") as in_file:
    plik = in_file.read()
    changes = re.sub(
        r"([a-zA-ZżźćńółęąśŻŹĆĄŚĘŁÓŃ]*)((obsr(y|a|w))+|((kur(w|ew|est))+|(jeb(a|i|c|m|n|l|))+|(sukin)+|(pie(rd|prz))+|(kuta(s|f))+|(pi(z|ź)d)+|(downi)+|(smierdziel)+|(spermosior)+|(huj)+|(picz)+|(mord(a|e))|(dup(a|e|y|i|c))+|(fuck)+|(szmato)+|(korwa)|(ciul)+|(fiu(t|c))+|(dzif)+|(debil)|(ciota)|(zapier)+|(sr(a|ywa))|(rucha)+|(cip)+|(dziwk)))([a-zA-ZżźćńółęąśŻŹĆĄŚĘŁÓŃ]*)",
        "---", plik)
file = open(
    'N:/5.semestr/PJN/cw3/wulgarneslowa_changed.txt', "a", encoding="utf-8")
file.write(changes)
