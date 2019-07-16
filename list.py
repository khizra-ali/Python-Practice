#list

employee_list = ["umair", "ali", "amir", "danish", "hamza", 5,7,8]
employee_age = [22,33,23,26,28]
print(employee_list)
print("employee name is: "+str(employee_list[6]))
print("employee name is: "+str(employee_list[7]))
print("employee name is: "+str(employee_list[1]) +"employee age is: "+ str(employee_age[1]))
employee_data = ["umair", 22 , "karachi"]
employee_data.append("Pakistan") #add value in last
print(employee_data)
employee_data[2] = "Lahore" #edit 2nd index value
print(employee_data)
employee_data.insert(1, "khan") #insert value at 1st index
print(employee_data)
employee_data.pop() #remove last index value
print(employee_data)
del employee_data[1] #delete value of mentioned index
print(employee_data)
employee_list.remove("ali") #removve any value you mention
print(employee_list)

