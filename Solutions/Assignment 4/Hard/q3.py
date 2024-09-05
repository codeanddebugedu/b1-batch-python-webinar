n = int(input("Enter a number = "))

# Loop through all possible factors from 1 to n
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")  # If i is a factor, print it
