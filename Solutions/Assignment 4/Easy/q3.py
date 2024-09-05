n = int(input("Enter a number = "))

number = 1

# Loop n times to generate the sequence
for i in range(n):
    # Print the current number
    print(number, end=" ")

    # Adjust the number for the next iteration
    if i % 2 == 0:
        number += 2  # Increase by 2 on even index
    else:
        number += 3  # Increase by 3 on odd index
