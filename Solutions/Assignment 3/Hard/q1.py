num = int(input("Enter a number = "))

# Initialize digit count to 0
count = 0

# Use a loop to count the digits by continuously dividing the number by 10
while num != 0:
    num //= 10  # Divide the number by 10 to remove the last digit
    count += 1  # Increment the count

print(f"Total digits = {count}")
