num = int(input("Enter a number = "))

# Loop to reduce the number by removing one digit each time
while num > 0:
    print(num, end=" ")
    num = num // 10  # Remove the last digit by integer division
