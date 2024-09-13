def highest_frequency(lst: list[int]) -> int:
    if len(lst) == 0:
        return 0
    frequency = {}
    highest_freq = 0
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
        if frequency[num] > highest_freq:
            highest_freq = frequency[num]
    return highest_freq


print(highest_frequency([1, 2, 2, 3, 3, 3, 4]))
print(highest_frequency([5, 5, 5, 1, 1, 2]))
print(highest_frequency([7, 8, 9, 10]))
print(highest_frequency([]))
