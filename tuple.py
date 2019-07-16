days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
print(days)
#del days(1) , can't call delete function
#days.append("saturday") , can't append
print(days[1])
days = list(days)
days[0]="sunday"
print(days)
days = tuple(days)
print(days)
for day in range(0,len(days)):
    if days[day] =="sunday":
         print("its holiday")
    else:
        print("you've to go to work")