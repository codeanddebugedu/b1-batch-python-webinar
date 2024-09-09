# Q7. Reverse the list
my_list = [4, 8, 6, 5, 3, 12, 1, 3, 15, 10]
reversed_list = []
for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])
print(reversed_list)
