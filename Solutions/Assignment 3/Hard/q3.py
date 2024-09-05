num = int(input("Enter a number = "))

# Store the original number for comparison
original_num = num

# Initialize the reversed number to 0
reversed_num = 0

# Use a loop to reverse the number
while num != 0:
    last_digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + last_digit  # Append to reversed number
    num //= 10  # Remove the last digit

# Check if the reversed number is the same as the original number
if reversed_num == original_num:
    print("Yes")
else:
    print("No")
