def tosquares(a,b):
    for x in range(a,b):
        yield x**2

for val in tosquares(int(input("from: ")), int(input("to: "))):
    print(val, end=", ")
