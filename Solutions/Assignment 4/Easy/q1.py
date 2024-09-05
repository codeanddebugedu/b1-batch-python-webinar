n = int(input("Enter a number = "))

# Start a loop from 1 to n (inclusive)
for i in range(1, n + 1):
    # Print 10 raised to the power of the current value of i
    # This creates values like 10, 100, 1000, etc.
    print(10**i, end=" ")
