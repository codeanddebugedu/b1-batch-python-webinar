"""
Enter a number = 5
1
2
4
8
16

Enter a number = 8
1
2
4
8
16
32
64
128

Enter a number = 3
1
2
4
"""

ans = 1
num = 8
for i in range(1, num + 1):
    print(ans)
    ans = ans * 2
