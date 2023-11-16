def prime(n):
    is_prime = True
    for i in (2,n-1):
        if n%i == 0:
           is_prime = False
    if is_prime:
        print("Its a prime number")
    else:
        print("Its not a prime number")


n=int(input("Enter the number:"))
prime(n)

