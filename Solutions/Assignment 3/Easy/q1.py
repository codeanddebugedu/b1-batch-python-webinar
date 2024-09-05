# We want to count numbers divisible by 5 but not by 10 between 20 and 240.
# We'll use a while loop and a single if statement to accomplish this.

# Initialize the starting point and the counter
i = 20
count = 0

# Loop until the number exceeds 240
while i <= 240:
    # Check if the number is divisible by 5 but not divisible by 10 in a single condition
    if i % 5 == 0 and i % 10 != 0:
        # If the condition is true, increase the count
        count += 1

    # Move to the next number
    i += 1

print(f"Count of numbers divisible by 5 but not by 10 = {count}")
