import os

put = input("Path: ")

if os.path.exists(put):
    print("Exists: deleting")
    os.remove(put)

else:
    print("Does not exist")
