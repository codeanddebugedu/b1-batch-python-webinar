def generate_cubes(n: int) -> dict[int, int]:
    cubes_dict = {}
    for i in range(1, n + 1):
        cubes_dict[i] = i**3
    return cubes_dict


# Alternate Way
# def generate_cubes(n: int):
#     cubes_dict = {i: i**3 for i in range(1, n + 1)}
#     return cubes_dict


print(generate_cubes(5))
print(generate_cubes(3))
print(generate_cubes(0))
print(generate_cubes(1))
