def greet(): #funct define
    print("Good Morning")
greet() #fucntion calling
greet() #no matter how many times we can now just use this to call greet
print("I'm outisde the function")
greet()
print("completed")

# def add():
#     a=2
#     b=3
#     my_sum= a+b
#     print(my_sum)
# add()

c=int(input("enter number 1: "))
d=int(input("enter number 2: "))
def add(num1,num2): #receiving information/data
    my_sum=c+d
    print(my_sum)
add(c,d) #passing data called arguments

c=int(input("enter number 1: "))
d=int(input("enter number 2: "))
def subtract(num1,num2): #receiving information/data
    minus=abs(c-d)
    print(minus)
subtract(c,d) #passing data called arguments

c=int(input("enter number 1: "))
d=int(input("enter number 2: "))
def multiply(num1,num2): #receiving information/data
    multiplication=c*d
    print(multiplication)
multiply(c,d) #passing data called arguments

c=int(input("enter number 1: "))
d=int(input("enter number 2: "))
def divide(num1,num2): #receiving information/data
    division=c/d
    print(division)
divide(c,d) #passing data called arguments

def my_pet(owner,pet, city="Karachi"):
    print(owner, "is an owner of", pet, "they are from ", city )
my_pet("John","Rabbit") 
my_pet(pet="Cat", owner="ali", city="Lahore" ) # here you dont have to consider position

#There are 4 types of functions
#1. takes nothing return nothing
#2. takes sth return nothing
#3. takes nothing return sth
#4. takes sth return sth

#type 3
# def sum():
#     a=2
#     b=3
#     return (a+b)
# result = sum()
# print(results)

#type 4
# def sum(val1, val2):
#     result=val1+val2
#     return result
# output_of_function = sum(a,b)
# print(output_of_function)

value1=int(input("enter a number "))

def check(val1):
    if (val1%2) == 0:
        return("even")
    else:
        return("odd")
check(value1)

def pizza(crust, **topping): # single * steric is for tuple and double ** for dictionaries
    print("You have ordered a pizza with", crust, "crust and the following toppings")
    for key,value in topping.items():
        print(key, ":", value)
pizza("Thick", topping1="Green Olives",topping2="Chicken", topping3="black olives")