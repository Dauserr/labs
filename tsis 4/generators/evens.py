def onlyeven(n):
    for x in range(0,n):
        if x%2==0:
            yield x

for val in onlyeven(int(input("from 0 to: "))):
    print(val, end=", ")
