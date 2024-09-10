# lst[0], lst[-1] = lst[-1] = lst[0]  # Method 1


my_list = ["Anirudh", 6, 4, 110.654, True, -54]
print(my_list)

temp = my_list[0]
my_list[0] = my_list[-1]
my_list[-1] = temp

print(my_list)
