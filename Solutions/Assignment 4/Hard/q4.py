n = int(input("Enter a number = "))

# Assume the number is prime until proven otherwise
is_prime = True

# Check for factors from 2 to sqrt(n)
for i in range(2, n):
    if n % i == 0:
        is_prime = False  # If a factor is found, the number is not prime

if is_prime:
    print("Yes")
else:
    print("No")
