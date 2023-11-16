#getting the input
score=input("Enter the list of scores:").split()
#intialize empty variable
hs=0
#loop
for i in score:
    #change the data value
    j=int(i)
    if j>hs:
        hs=j
    else:
        print("your input is not valid")
#print the value
if hs != 0:
    print(f"The highest score is {hs}")
