import re

txt = "alsadkasldkasldb aaaab ab ba a b asdashdjashdj jknjsdnjsadb absajdhajsdbajsdb"
splt = re.split("\s", txt)

for word in splt:
    x = re.findall("^a.*b$",word)
    print(x, end=", ")
