# Create a new list from two list using the following condition

# pseudocode

# Give the list
list1=[10, 20, 25, 30, 35]
list2=[40, 45, 60, 75, 90]

# Create new list
new_list=[num for num in list1 if num % 2!=0]+[num for num in list2 if num % 2==0]

# Print the new list
print (f"New list: {new_list}")
