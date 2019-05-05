num1=float (input("enter number 1: "))
num2=float (input("enter number 2: "))
operator=input("enter operator: ")

if operator == " + ":
   c=num1 + num2
   print("addition of two numbers",c)
elif operator == " - ":
    c=num1 - num2
    print("subtracting two numbers", c)
elif operator == " * ":
    c=num1 * num2
    print("multiply two numbers", c)
elif operator == " / ":
    c=num1 / num2
    print("divide two numbers", c)
else:
    print("null")