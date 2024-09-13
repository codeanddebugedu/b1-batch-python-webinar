# def add(n1, n2):
#     return n1 + n2

# add = lambda n1, n2: n1 + n2
# print(add(10, 20))


def maximum(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


maxii = lambda n1, n2: n1 if n1 > n2 else n2
print(maxii(10, 20))
