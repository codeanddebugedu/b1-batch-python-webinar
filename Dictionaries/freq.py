my_list = [5, 6, 5, 4, 5, 5, 5, 4, 3, 4, 3, 7, 6, 6, 6, 6, 6, 7, 6, 7, 1]


my_dictionary = {}

# for i in range(0, len(my_list)):
#     if my_list[i] in my_dictioary:
#         my_dictioary[my_list[i]] += 1
#     else:
#         my_dictioary[my_list[i]] = 1


for num in my_list:
    my_dictionary[num] = my_dictionary.get(num, 0) + 1
# {5: 5, 6: 7, 4: 3, 3: 2, 7: 3, 1: 1}
print(my_dictionary)

element = 0
max_count = 0

for k, v in my_dictionary.items():
    if v > max_count:
        max_count = v
        element = k


print(element)
print(max_count)
