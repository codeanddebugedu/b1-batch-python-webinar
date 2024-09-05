# Initialize the first number in the sequence
num = 1

# Initialize a counter to keep track of how many numbers we've printed
count = 0

# Use a while loop to print the sequence 10 times
while count < 10:
    print(num, end=" ")
    # Update the number by multiplying it by 2
    num *= 2
    count += 1
