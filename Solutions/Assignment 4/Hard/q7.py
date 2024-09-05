n = int(input("Enter a number = "))

# Loop to keep reducing the sum until a single digit is obtained
while n >= 10:
    sum_of_digits = 0
    while n > 0:
        digit = n % 10  # Get the last digit
        sum_of_digits += digit  # Add the digit to the sum
        n = n // 10  # Remove the last digit by integer division
    n = sum_of_digits  # Update n to be the sum of its digits

print(f"Single-digit sum = {n}")
