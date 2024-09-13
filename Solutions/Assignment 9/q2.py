def check_divisibility(a: int, b: int):
    if a % b == 0:
        print(True)
    else:
        print(False)


a = int(input("Enter the first integer (a) = "))
b = int(input("Enter the second integer (b) = "))
check_divisibility(a, b)
