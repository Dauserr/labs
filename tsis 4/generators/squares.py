def tosquares(n):
    for x in range(0,n):
        yield x**2

for val in tosquares(int(input("from 0 to: "))):
    print(val)
