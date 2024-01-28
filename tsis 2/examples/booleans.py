print(10>9)
print(10==9)
print(10<9)

##
##
a = 200
b = 33

if b>a:
    print ("b is  greater than a")
else:
    print("b is not greater than a")

##
##

print(bool("Hello"))
print(bool(15))

##
##

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

##
##

bool("abc") #true
bool(123) #true
bool(["apple", "cherry", "banana"]) #true

##
##

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) # these all are false, only something empty is false

##
##

class myclass(): #myclass - name of the class
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

##
##

def myFunction() :
  return True

print(myFunction())

##
##

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

##
##

x = 200
print(isinstance(x, int))#check if x is a type of int
