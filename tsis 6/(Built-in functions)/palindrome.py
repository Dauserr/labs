word = str(input("give me a word: "))

def ispalindrome(word):
    for i in range(0,len(word)):
        if word[i]==word[len(word)-i-1]:
            continue
        else:
            return False
    return True

if ispalindrome(word):
    print("Yes, its a palindrome")
else:
    print("No, its not a palindrome")
