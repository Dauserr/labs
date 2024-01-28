thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")# if the items does not exist there will be error

print(thisset)

#
#

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana") # if the items does not exist there will be not any error

print(thisset)

#
#

thisset = {"apple", "banana", "cherry"}

x = thisset.pop() # random delete

print(x)

print(thisset)

#
#

thisset = {"apple", "banana", "cherry"}

thisset.clear() # set is cleared

print(thisset)

#
#

thisset = {"apple", "banana", "cherry"}

del thisset

#print(thisset) set is deleted
