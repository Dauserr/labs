age = 36
#txt = "My name is John, I am" + age !!!!! wrong
#print(txt)

##
age = 36
txt = "My name is John, I am {}"
print(txt.format(age))
##
quantity = 3
itemno = 567
price = 49.96
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
##
quantity = 3
itemno = 567
price = 49.96
myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))
##
