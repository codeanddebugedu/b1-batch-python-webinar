"""
Pass by Reference (Mutables) (list,set,dictionary)
vs
Pass by Value (Immutable) (int,float,strings,tuple)
"""

# def change(a):
#     print(id(a))
#     a.append(6)


# a = [1, 2, 3, 4, 5]
# print(id(a))
# change(a)
# print(a)


def change(x):
    # x.update({"Anirudh": 99})
    print(x)


a = {"Anirudh": 100}
change(a)
print(a)
