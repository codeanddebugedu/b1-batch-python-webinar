"""
Ask start number = 1
Ask end number = 100

1+2+3+4...+9+10
55
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
total = 0
for i in range(start, end + 1):
    total = total + i

print(total)
