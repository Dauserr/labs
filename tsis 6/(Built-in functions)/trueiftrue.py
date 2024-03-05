tup = (";;","p")

def iftrue(tuple):
    for i in tuple:
        if i == False:
            return False
    return True

if iftrue(tup):
    print("True")
else:
    print("False")
