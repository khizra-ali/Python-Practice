inputdetails = input("enter your name")
with open("textfile.txt", "w") as f:
    f.write(inputdetails)
with open("textfile.txt", "a") as f:
    f.write("this is second line")

name = input(" enter.biodata of: ")
with open("biodata.txt", "w") as f:
    f.write("\n KHIZRA")
    f.write("\n 23")
    f.write("\n NIAZ ALI")

