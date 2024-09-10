# Method 1
# def reverselistLastNSlice(lst: List, n: int):
#     l = len(lst)
#     result = lst[l - n :]
#     result.reverse()
#     print(result)


my_list = ["Anirudh", 6, 4, 110.654, True, -54]

n = int(input("Enter n = "))
l = len(my_list)
result = my_list[: l - n - 1 : -1]
print(result)
