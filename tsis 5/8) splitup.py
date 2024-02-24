import re

txt = "WhyAreYouSittingOnTheCharger"
splt = re.findall("[A-Z][a-z]*", txt)
ssplt = re.split("[A-Z]", txt)

print(splt)
print(ssplt)
