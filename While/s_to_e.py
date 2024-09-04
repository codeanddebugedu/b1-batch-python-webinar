"""
Ask start from user = 10
Ask end from user = 14
10 11 12 13 14


Ask start from user = 91
Ask end from user = 102

91 92 93 94....99 100 101 102
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

i = start
while i <= end:
    print(i)
    i += 1
