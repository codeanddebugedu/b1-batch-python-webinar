# Q1. Even and Odd Count
my_list = [4, 8, 6, 5, 3, 12, 1, 3, 15, 10]
odd = 0
even = 0
for num in my_list:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Odd = {odd}")
print(f"Even = {even}")
