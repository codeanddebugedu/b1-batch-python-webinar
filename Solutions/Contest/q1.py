def sum_odd_and_even(lst):
    even = 0
    odd = 0
    for num in lst:
        if num % 2 == 0:
            even += num
        else:
            odd += num
    return [even, odd]
