# Q5. Remove duplicates
my_list = [4, 8, 8, 8, 3, 4, 4, 1, 4, 4, 1]
new_list = []
for num in my_list:
    if num not in new_list:
        new_list.append(num)
print(new_list)
