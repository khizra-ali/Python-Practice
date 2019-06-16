#Show two integars are either equal to each other or their sum or difference equal t 5

num1=int(input("Enter num 1: "))
num2=int(input("Enter num 2: "))

if num1 == num2 or (num1+num2) == 5 or abs(num1-num2) == 5:
    num_flag = True
    print(num_flag)
else:
    num_flag = False
    print(num_flag)