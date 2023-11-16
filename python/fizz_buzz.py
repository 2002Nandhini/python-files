for i in range(1,100):
    #both divisible by 3 and 5
    if (i%3==0) and (i%5==0):
        print("FIZZBUZZ")
    #divisible by 3 
    elif i%3==0:
        print("FIZZ")
    #divisible by 5
    elif i%5==0:
        print("BUZZ")
    else:
    #not divisible by 3 and 5
        print(i)
        
        
