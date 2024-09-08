my_list = [6] * 100000000
b = []

# n = len(my_list)
# for i in range(0, n):
#     if my_list[i] == 6:
#         my_list.pop(i)


# for num in my_list:
#     if num == 6:
#         my_list.remove(num)

# n^2
# while 6 in my_list:
#     my_list.remove(6)

# n
for num in my_list:
    if num != 6:
        b.append(num)

print(my_list)
print(b)
