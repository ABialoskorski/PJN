import re

zdanie =  input("Napisz coś o sobie, program może zawierać wulzaryzmy (I tak je zastąpii --- ;)\n")
print("Twoje zdanie przed: ", zdanie)
noweZdanie = re.sub(r'c?huj(a|ek|u|em|nia|owy|owa|owe)?|cip(a|ę|e|ą)|(do)?jeb(ać|ac|ie|ał|al|ała|ałem|ał|ię)|(do)?pieprz(ać|ac)|(do)?pierd(alać|ala|alał|oli|olił|olę|olić)|dup(a|ą|eczka|ie)|(do|na)?jeb(ać|ał|ie|ak|ać|any|ane|ak|anka|anko|any|nąć)?|kur(estwo|wa|ew|ewski|wy|ewska|wiska|wić|wiszon|wiki|wiszony|wo)|kutas(|a|ie|em|y|ami|ów)', '---', zdanie.lower())
print("Twoje zdanie po: ", noweZdanie)
