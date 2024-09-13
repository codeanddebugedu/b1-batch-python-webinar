def remove_duplicates(lst):
    unique_list = []
    for num in lst:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates([5, 5, 5, 5, 5]))
print(remove_duplicates([10, 20, 30, 10, 40, 50, 20]))
print(remove_duplicates([]))
print(remove_duplicates([1, 2, 3, 1, 4, 3, 2]))
