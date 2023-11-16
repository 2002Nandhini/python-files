'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
'''

def numoflist(l):

    if not l:
        return 0
    else:
        return 1+numoflist(l[1:])

l=[1,2,3,4,5,4,5]
print(numoflist(l))
