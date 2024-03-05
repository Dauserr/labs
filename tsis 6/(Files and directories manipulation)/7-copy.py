pat = input("Path: ")
f = open(pat, "r")
content = f.read()
f.close()
pat2 = input("Path number two: ")
f = open(pat2, "w") #creates new file if it does not exist
f.write(content)
f.close()
