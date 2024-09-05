n = int(input("Enter a number = "))

# Initialize the first two Fibonacci numbers
prev = 0
next = 1

# Loop to generate and print the Fibonacci sequence up to n terms
for i in range(n):
    print(prev, end=" ")
    temp = next
    next = next + prev
    prev = temp
