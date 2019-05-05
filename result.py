English=int(input("enter obtained marks in English: "))
Pak_Studies=int(input("enter obtained marks in Pakistan Studies: "))
Sindhi=int(input("enter obtained marks in Sindhi: "))
Chemistry=int(input("enter obtained marks in Chemistry: "))
Biology=int(input("enter obtained marks in Biology: "))

obtained_marks=English+Pak_Studies+Sindhi+Chemistry+Biology
print(obtained_marks)
total_marks=int(input("enter total marks: "))

percentage=(obtained_marks/total_marks)*100
print(percentage)
if percentage >= 80:
    print("Grade is A+")
elif percentage >= 70:
    print("Grade is A")
elif percentage >= 60:
    print("Grade is B")
elif percentage >= 50:
    print("Grade is D")
    
else:
    print("Fail")