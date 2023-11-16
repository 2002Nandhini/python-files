'''
#find sum of numbers is zero or not
def list_num(l):
    s=l
    for i in l:
        if -i in s:
            print(i)
    

l=[1,2,-1,3,-2]
print(list_num(l))
'''

def palindrome(s):
    li=''
    for i in range(len(s)-1,-1,-1):
        li+= s[i]
    print(li)

s='nandhini'
palindrome(s)

