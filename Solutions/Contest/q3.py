def list_of_multiples(num, length):
    return [i * num for i in range(1, length + 1)]


# Method 2
# def list_of_multiples(num, length):
#     lst = []
#     for i in range(length):
#         lst.append(num + i * num)
#     return lst
