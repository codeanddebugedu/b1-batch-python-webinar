"""
Ask start from user = 1
Ask end from user = 10
1
2
3
...
9 
10


Ask start from user = 17
Ask end from user = 11
11
12
13
...
16
17
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))


if start < end:
    i = start
    j = end
else:
    i = end
    j = start

while i <= j:
    print(i)
    i += 1
