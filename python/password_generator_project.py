#importing random module
import random
characters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')']
print("WELCOME TO THE PASSWORD CREATOR")
#getting the input
ch=int(input("How many characters you want :"))
num=int(input("How many numbers you want :"))
sym=int(input("How many Symbols you want :"))

n=ch+num+sym
a=""
b=""
for i in range(1,ch+1):
    a+=random.choice(characters)
for i in range(1,num+1):
    a+=random.choice(numbers)
for i in range(1,sym+1):
    a+=random.choice(symbols)
#syntax mtd
#print(''.join(random.choices(a + b +c,k=n)))
#2nd mtd
print(a)
#for mtd
for i in range(1,n+1):
    b+=random.choice(a)
print(b)



