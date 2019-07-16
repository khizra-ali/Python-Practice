""" Inventory Series 
2. Inventory Sales:
a. create a function for getting order
b. create a bill function for bill calculation
c. create a function for discout offer:
               
    if bill is more than 5000 offer 50% discout
    if bill is more than 2500 or equal to 25000 offer 25% discount
    else no discount"""
#pizza hut
#a.
input1= input("What flavor do you want: ")
input2=input("what toppings do you want: ")
input3=input("what crust do you want: " )
def order(flavour, toppings, crust):
    print("Your order is flavour", input1,", toppings", input2, "and crust", input3)
order(input1,input2,input3)

#b.
def bill_calculation(input1, input2, input3):
    bill_calculation(input1=500)