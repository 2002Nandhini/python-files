#enter the numbers
a=input("Enter the list of numbers:").split()
#calculate the sum of number
sum=0
for n in a:
    i=int(n)
    sum=sum+i
print(f"The sum values are:{sum}")
#calculate the length
l=0
for i in a:
    l+=1
print(f"The len of values are:{l}")
#calculate the average
print("The height average is ",sum/l)

