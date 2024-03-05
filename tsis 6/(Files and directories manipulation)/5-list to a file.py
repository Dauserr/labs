pat = input("Path: ")
f = open(pat, "w")

dannye = "[1,2,3,4,5]"
f.write(dannye)
f.close()

f = open(pat, "r")
print("after writing: ",f.read())
