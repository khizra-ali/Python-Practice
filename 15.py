Amount=int(input("Enter amount: "))
Interest=float(input("Enter value: "))*0.01
print(Interest)
Years=int(input("Enter no of years: "))
Future_value=round(Amount*((1+Interest)**Years),2)
print(Future_value)