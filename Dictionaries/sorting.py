my_list = [5, 6, 5, 4, 5, 4, 3, 4, 3, 7, 6, 6, 6, 6, 6, 7, 7, 6, 7, 1]
my_dictionary = {}

for num in my_list:
    my_dictionary[num] = my_dictionary.get(num, 0) + 1

print(my_dictionary)
print(my_dictionary.items())

ans = dict(sorted(my_dictionary.items(), key=lambda x: x[1], reverse=True))
print(ans)
