import os

put = input("Path: ")

if os.path.exists(put):
    print("Exists, content:")
    print(os.listdir(put))
    print("name:", put)
else:
    print("Does not exist")
