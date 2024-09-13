def total_cups(n: int):
    free_cups = n // 6
    total = n + free_cups
    print(total)


n = int(input("Enter the number of cups bought = "))
total_cups(n)
