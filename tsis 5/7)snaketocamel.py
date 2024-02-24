import re

txt = "why_are_you_sitting_on_the_charger"

x = re.split("_",txt)
camel = x[0] + "".join(word.capitalize() for word in x[1:])

print(camel)
