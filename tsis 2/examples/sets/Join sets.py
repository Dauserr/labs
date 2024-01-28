set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) # creates new set
print(set3)

#
#

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#
#

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y) #only intersection

print(x)

#
#

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) # new intersection set

print(z)

#
#

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y) # remove all same values

print(x)

#
#

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y) # same as previous but new set

print(z)

#
#

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y) # remove all '1'`s and 'True' since they are equal and creates new set

print(z)
