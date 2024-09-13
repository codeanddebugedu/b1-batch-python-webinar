def simple_calculator(num1: int, num2: int, operation: str):
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    else:
        print("Invalid operation")


num1 = int(input("Enter the first number = "))
num2 = int(input("Enter the second number = "))
operation = input("Enter the operation ('+' for addition or '-' for subtraction) = ")

simple_calculator(num1, num2, operation)
