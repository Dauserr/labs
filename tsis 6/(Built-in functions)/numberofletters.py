predl = str(input("give me a sentence: "))
up = 0
lower = 0
for i in range(0,len(predl)):
    if predl[i] == " ":
        continue
    if predl[i].isupper():
        up+=1
    else:
        lower+=1

print("number of uppers: ", up)
print("number of lowers: ", lower)
