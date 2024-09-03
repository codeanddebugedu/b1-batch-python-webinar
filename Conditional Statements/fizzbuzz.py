"""
FizzBuzz
Ask a number from user

divisible by 3 -> FIZZ
divisible by 5 -> BUZZ
divisible by 3 and 5 -> FIZZBUZZ

else

FIZZFIZZBUZZBUZZ
"""

num = int(input("Enter your num = "))
if num % 3 == 0 and num % 5 == 0:
    print("FIZZBUZZ")
elif num % 3 == 0:
    print("FIZZ")
elif num % 5 == 0:
    print("BUZZ")
else:
    print("FIZZFIZZBUZZBUZZ")
