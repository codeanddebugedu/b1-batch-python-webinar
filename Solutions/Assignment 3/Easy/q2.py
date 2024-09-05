start = int(input("Enter the starting number = "))
end = int(input("Enter the ending number = "))

# Initialize the sum to 0
total_sum = 0

i = start

# Loop through the numbers from start to end (inclusive)
while i <= end:
    # Check if the number is divisible by both 3 and 6 but not by 9
    if i % 3 == 0 and i % 6 == 0 and i % 9 != 0:
        # If the condition is true, add the number to the total sum
        total_sum += i

    # Move to the next number
    i += 1

print(f"The total sum of numbers divisible by 3 and 6 but not 9 is = {total_sum}")
