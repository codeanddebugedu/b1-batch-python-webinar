"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
