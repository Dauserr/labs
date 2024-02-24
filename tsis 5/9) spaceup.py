import re

txt = "WhyAreYouSittingOnTheCharger"
splt = re.findall("[A-Z][a-z]*", txt)

for word in splt:
    print(word, end=" ")
