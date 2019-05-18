list = []
num = int(input("How many numbers: "))
for n in range(num):
    numbers = int(input("Enter number "))
    list.append(numbers)
print("Maximum element in the list is :", max(list))
max_index=list.index(max(list))
print("Index of Max no: ", max_index)
print("\n Minimum element in the list is :", min(list))
min_index=list.index(min(list))
print("Index of Max no: ", min_index)
add=sum(list)
mean=add/len(list)
print("Mean is: ", mean)