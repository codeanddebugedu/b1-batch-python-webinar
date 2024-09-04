"""
Ask start from user = 1
Ask end from user = 10
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
total = 0
i = start
while i <= end:
    total = total + i
    i += 1
print(total)
