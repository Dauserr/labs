import re

txt = "WhyAreYouSittingOnTheCharger"

x = re.findall("[A-Z][a-z]*", txt)

snake = x[0] + "_" + "_".join(word.lower() for word in x[1:])

print(snake)
