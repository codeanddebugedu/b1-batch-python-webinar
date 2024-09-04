"""
568 --- 1098

4 and 7 divisible,,,count them
"""

count = 0
i = 568
while i <= 1098:
    if i % 4 == 0 and i % 7 == 0:
        count = count + 1
    i += 1

print(count)
