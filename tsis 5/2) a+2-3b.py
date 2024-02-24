import re

txt = "abbbbbbbbb ab abb abbba"
splt = re.split("\s", txt)

for word in splt:
    x = re.findall("a+b{2,3}",word)
    print(x, end=", ")
