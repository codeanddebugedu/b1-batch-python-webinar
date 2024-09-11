"""
Args and Kwargs
"""


def add(*nums):
    n = len(nums)
    total = 0
    for i in range(0, n):
        total = total + nums[i]
    print(total)


add(10, 20)
