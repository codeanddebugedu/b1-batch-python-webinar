for i in range(5, 0, -1):
    for j in range(1, i + 1):
        if j % 2 == 1:
            print(1, end=" ")
        else:
            print(2, end=" ")
    print()
