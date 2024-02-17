def fromto0(n):
    for x in range(n,-1,-1):
        yield x

for val in fromto0(int(input("give me n: "))):
    print(val, end=", ")
