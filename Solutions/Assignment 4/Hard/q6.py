n = int(input("Enter a number = "))

# Loop to print the triangle of numbers
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Move to the next line after each row
