n = int(input("Enter a number = "))

ans = 10
for i in range(1, n + 1):
    print(ans + 1, end=" ")
    ans = ans * 10
