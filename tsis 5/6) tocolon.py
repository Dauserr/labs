import re

txt = "what are this imn the, tbaals,. dowakjdoawk d."

x = re.sub("\.|\s|,",":",txt)
print(x)
