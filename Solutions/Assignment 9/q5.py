def is_curzon(num: int):
    power_part = 2**num + 1
    product_part = 2 * num + 1
    if power_part % product_part == 0:
        print(True)
    else:
        print(False)


num = int(input("Enter a non-negative integer = "))
is_curzon(num)
