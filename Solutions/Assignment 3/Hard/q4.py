num = int(input("Enter a number = "))

original_num = num

# Find the number of digits
digit_count = 0
temp = num
while temp != 0:
    temp //= 10
    digit_count += 1

# Initialize a variable to store the sum of powers
sum_of_powers = 0

# Calculate the sum of each digit raised to the power of the number of digits
temp = num
while temp != 0:
    last_digit = temp % 10
    sum_of_powers += last_digit**digit_count
    temp //= 10

# Check if the sum of powers is equal to the original number
if sum_of_powers == original_num:
    print("Yes")
else:
    print("No")
