from datetime import date
print("enter date in format: DD/MM/YYYY")

D1,M1,Y1 = (input("enter first date: ")).split("/")
D2,M2,Y2 = (input("enter second date: ")).split("/")
D1=int(D1)
M1=int(M1)
Y1=int(Y1)
D2=int(D2)
M2=int(M2)
Y2=int(Y2)
date1=date(Y1,M1,D1)
date2=date(Y2,M2,D2)
Days_between_2_dates=date2-date1
print(Days_between_2_dates)
