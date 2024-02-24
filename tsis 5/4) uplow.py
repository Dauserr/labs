import re

txt = "Aaasdaosdkaspodk rwefeo kfsoe SFDSAOKSDsaldksald"
splt = re.split("\s", txt)

for word in splt:
    x = re.findall("[A-Z][a-z]+",word)
    print(x, end=", ")
