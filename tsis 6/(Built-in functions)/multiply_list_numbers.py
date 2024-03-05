lst = []
n = int(input("size of list: "))
for i in range(0,n):
    lst.append(int(input()))
print(lst)

mb = int(input("multiply by: "))

for i in range(0,n):
    lst[i]*=mb

print(lst)
