def return_unique(my_list: list[int]) -> list:
    frequency = {}
    for num in my_list:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    result = []
    for num, freq in frequency.items():
        if freq == 1:
            result.append(num)
    return result


print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
