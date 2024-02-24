import re

txt = "bbbbbba abbbb abab"
#with open("labs/tsis 5/row.txt","r", encoding="utf-8") as file:
#    content = file.read()
splt = re.split("\s", txt)

for word in splt:
    x = re.findall("a+[b]*",word)
    print(x, end=", ")
