def divis(n):
    for x in range(0,n):
        if x%3==0 and x%4==0:
            yield x

for val in divis(int(input("from 0 to: "))):
    print(val, end=(", "))
