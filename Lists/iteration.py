"""
Iteration
"""

my_list = [5, 6, 4, 7, 2, "Aniryudh", 66.77, True]

n = len(my_list)
for i in range(0, n):
    print(my_list[i], end=" ")

# for i in range(n - 1, -1, -1):
#     print(my_list[i], end=" ")

# Iterate by value
for ele in my_list:
    print(ele)
