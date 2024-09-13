def find_largest(num1: int, num2: int, num3: int):
    if num1 >= num2 and num1 >= num3:
        print(num1)
    elif num2 >= num1 and num2 >= num3:
        print(num2)
    else:
        print(num3)


num1 = int(input("Enter the first number = "))
num2 = int(input("Enter the second number = "))
num3 = int(input("Enter the third number = "))

find_largest(num1, num2, num3)
