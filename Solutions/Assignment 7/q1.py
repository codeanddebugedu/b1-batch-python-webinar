my_list = ["Anirudh", 6, 4, 110.654, True, -54]

start = int(input("Enter start = "))
end = int(input("Enter end = "))

result = []
for i in range(start, end + 1):
    result.append(my_list[i])
print(result)
