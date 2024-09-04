"""
Ask start from user = 1
Ask end from user = 10

1 to 10---2,4,6,8,10 ---> 30
1 to 10---1,3,5,7,9 ----> 25

Even sum = 30
Odd sum = 25
"""

start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
even_sum = 0
odd_sum = 0
i = start
while i <= end:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    i += 1

print(even_sum)
print(odd_sum)
