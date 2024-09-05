# Ask the user for the number
num = int(input("Enter a number = "))

factorial = 1
i = num

# Loop until current reaches 1
while i > 0:
    factorial *= i  # Multiply the i number with factorial
    i -= 1  # Move to the next lower number

print(f"Factorial of {num} is {factorial}")
