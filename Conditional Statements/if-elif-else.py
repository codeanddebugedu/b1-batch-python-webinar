"""
ELIF
Ask Age  from user
18 or 18 above -> ADULT
12-17 -> Teenager
11 below -> Child
"""

age = int(input("Enter your age = "))
if age >= 18:
    print("Adult")
elif age >= 12 and age <= 17:
    print("Teenager")
elif age >= 0 and age <= 11:
    print("Child")
else:
    print("Invalid")
