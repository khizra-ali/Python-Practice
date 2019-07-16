#prime
no=int(input("enter number:"))
if no <= 0 or no == 1:
    print(no, "is not prime")
elif no == 2:
    print(no, "is prime")
else:
    iter = 2
    is_prime = True
    for i in range(2,no):
        iter += 1
        if no % i == 0:
            break
    if iter == no:
        print(no, "is prime")
    else:
        print(no, "is not prime")

#prime by using flag
no=int(input("enter number:"))
if no <= 0 or no == 1:
    print(no, "is not prime")
elif no == 2:
    print(no, "is prime")
else:
    is_prime = True
    for i in range(2,no):
        print(i)  #numbers by which it is trying to divide
        if no % i == 0:
            is_prime = False
            break #loop terminate like 9/3 loop will break here 
    if is_prime:
            print(no, "prime number")
    else:
            print(no, "is not prime number")
