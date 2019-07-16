
# for i in range(10): #start from 1 up to 9
#     print(i)
#     print("hello")


#for i in range(2,10): #start from 2 upto 9
#     print(i)
#     print("bye")

import random
arr = []
for i in range(2,10): #start from 2 upto 9
   arr.append(random.randint(1,100))
for num in arr:
    print(num)
 #table
number= int(input("enter value"))
for i in range(1,11):
     print (number, "x", i, "=", str(number*i))


