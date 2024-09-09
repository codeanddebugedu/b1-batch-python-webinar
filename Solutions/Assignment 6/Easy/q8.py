# Q8. Remove number if exists
my_list = [4, 8, 8, 8, 3, 4, 4, 1, 4, 4, 1]
num_to_remove = int(input("Enter a number = "))
if num_to_remove in my_list:
    my_list.remove(num_to_remove)
    print(my_list)
else:
    print("Invalid")
