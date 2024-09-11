def add(num1, num2):
    total = num1 + num2
    print(f"Add = {total}")


def sub(num1, num2):
    total = num1 - num2
    print(f"Sub = {total}")


def mul(num1, num2):
    total = num1 * num2
    print(f"Mul = {total}")


def div(num1, num2):
    total = num1 / num2
    print(f"Div = {total}")


x = int(input("Enter a num 1 = "))
y = int(input("Enter a num 2 = "))
add(x, y)
sub(x, y)
mul(x, y)
div(x, y)
