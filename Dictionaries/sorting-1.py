my_list = [
    ["Anirudh", 23, 56, 45],
    ["Sanjay", 78, 63, 11],
    ["Muskan", 89, 99, 100],
    ["Prakhar", 56, 54, 91],
    ["Vandana", 97, 54, 32],
]

# print(list(sorted(my_list, key=lambda x: x[3])))
print(list(sorted(my_list, key=lambda x: x[1] + x[2] + x[3])))
