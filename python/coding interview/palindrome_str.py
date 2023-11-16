def ispalindrome(l):

    a=l.lower()

    for i in range(int(len(a)/2)):
        if a[i] == a[len(a)-i-1]:
            return True
        else:
            return False

c='abcba'
print(ispalindrome(c))

            
