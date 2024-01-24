x = "pytHon caSe"
print(x.capitalize()) # first letter to upper and all other to lower

##
x = "pytHON caSe"
print(x.casefold()) # full to lower

##
txt = "banana"
x = txt.center(20)
print(x)
##
txt = "banana"
x = txt.center(20, "O")
print(x)
##
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
##
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24) ## from to
print(x)
##
txt = "My name is St å le"
x = txt.encode()
print(x)
##
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
##
txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11) # from to
print(x)
##
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2) # convert tab to given amount of whitespaces
print(x)
##
txt = "Hello, welcome to my world."
x = txt.find("welcome") # return index when the word is starting
print(x)
##
txt = "Hello, welcome to my world."
print(txt.find("q")) # return -1 if q is not given
##
