# Ask the user for the start and end numbers
start = int(input("Enter start number = "))
end = int(input("Enter end number = "))

# Initialize a temporary variable for the current number
current = start

# If start is less than or equal to end, print numbers in ascending order
if start <= end:
    while current <= end:
        print(current, end=" ")
        current += 1
else:
    # If start is greater than end, print numbers in descending order
    while current >= end:
        print(current, end=" ")
        current -= 1
