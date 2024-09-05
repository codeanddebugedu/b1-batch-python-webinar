num = int(input("Enter a number = "))

# Initialize the reversed number to 0
reversed_num = 0

# Use a loop to reverse the digits
while num != 0:
    last_digit = num % 10  # Get the last digit of the number
    reversed_num = (
        reversed_num * 10 + last_digit
    )  # Append the last digit to the reversed number
    num //= 10  # Remove the last digit from the original number

print(f"Reversed number = {reversed_num}")
