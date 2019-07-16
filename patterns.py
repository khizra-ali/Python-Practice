#41
print("-------------------41-HALF DIAMOND------------------")
num=int(input("enter no of rows: "))
for i in range(0,num):
    for j in  range(0,i+1):
        print("*", end=" ")
    print()
for i in range(num-1,0,-1):
    for j in range(1,i+1):
         print("*", end=" ")
    print()
#42
print("-------------------42-HALF DIAMOND IN NUMBERS------------------")
num=int(input("enter no of rows: "))
for i in range(0,num+1):
    for j in  range(1,i+1):
        print(j, end=" ")
    print()
for i in range(num-1,0,-1):
    for j in range(1,i+1):
         print(j, end=" ")
    print()

#43
print("-------------------43-NUMBERS------------------")
num=int(input("enter no of rows: "))
for i in range(0,num+1):
    for j in  range(1,i+1):
        print(i, end=" ")
    print()
# for i in range(num-1,0,-1):
#     for j in range(1,i+1):
#          print(i, end=" ")
#     print()

print("-------------------43-Diamond------------------")
num=int(input("enter no of rows: "))
for line in range(0,num):
    for space in  range(line,num-1):
        print(" ", end=" ")
    for star in range()
       