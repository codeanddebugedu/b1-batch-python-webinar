my_dictionary = {
    "Anirudh": 78,
    "Nihar": 97,
    "Muskan": 45,
    "Prakhar": 43,
    "Ankit": 11,
}

print(my_dictionary.items())

# for k in my_dictionary:
#     print(k, my_dictionary[k])

# for k in my_dictionary.keys():
#     print(k)

# for v in my_dictionary.values():
#     print(v)

for k, v in my_dictionary.items():
    print(f"key = {k} and value = {v}")
