# Q4. Maximum from the list

# Method 1
my_list = [4, 8, 6, 5, 3, 12, 1, 3, 15, 10]
max_num = my_list[0]
for num in my_list:
    if num > max_num:
        max_num = num
print(max_num)

# Method 2 (Using max function) (Mostly used in DSA)
my_list = [4, 8, 6, 5, 3, 12, 1, 3, 15, 10]
max_num = my_list[0]
for num in my_list:
    max_num = max(max_num, num)
print(max_num)
