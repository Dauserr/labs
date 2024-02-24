import re

txt = "aosdkaspodk_asasdsadas aosdasokd_sadlkaslkd a_a A_A"
splt = re.split("\s", txt)

for word in splt:
    x = re.findall("[a-z]+_[a-z]+",word)
    print(x, end=", ")
