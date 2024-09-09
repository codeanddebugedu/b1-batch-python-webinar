"""
Start =
End = 

2 and 7 

Count
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
ans = [i for i in range(start, end + 1) if i % 2 == 0 and i % 7 == 0]
print(ans)
