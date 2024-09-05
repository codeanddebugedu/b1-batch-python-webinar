"""
Enter a number = 5
1
11
111
1111
11111

Enter a number = 8
1
11
111
1111
11111
111111
1111111
11111111

Enter a number = 3
111
1111
11111
"""

ans = 1
num = 5
for i in range(1, num + 1):
    print(ans)
    ans = (ans * 10) + 1
