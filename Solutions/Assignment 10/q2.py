def avg(a: int = 0, b: int = 0, c: int = 0, d: int = 0, e: int = 0) -> float:
    total = a + b + c + d + e
    return total / 5


print(avg(1, 2, 3, 4, 5))
print(avg(10, 20))
print(avg())
print(avg(5, 15, 25))
print(avg(-1, -2, -3, -4, -5))
