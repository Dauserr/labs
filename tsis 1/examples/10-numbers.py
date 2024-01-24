x = 1 #int
y = 2.8 #float
z = 1j #complex
##
print(type(x))
print(type(y))
print(type(z))
##
x = 1
y = 12309129803910872987132
z = -712837812387

print(type(x))
print(type(y))
print(type(z))
##
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
##
x = 35e3
x = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
##
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
##
x = 1 # int
y = 2.8 #float
z = 1j #complex

#from int to float
a = float(x)

#from float to int
b = int(y)

#from int to complex
c = complex(x)

print(a)
print(b)
print(c)

##
import random
print(random.randrange(1, 10))
