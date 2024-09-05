num = int(input("Enter a number = "))

# Initialize the sum variable
sum_of_digits = 0

# Loop through the number and extract each digit using division and modulus
while num > 0:
    digit = num % 10  # Get the last digit of the number
    sum_of_digits += digit  # Add the digit to the sum
    num = num // 10  # Remove the last digit by integer division

print(f"Sum of digits = {sum_of_digits}")
