def maxi(a: int, b: int, c: int) -> int:
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


print(maxi(5, 10, 3))
print(maxi(-1, -5, -3))
print(maxi(0, 0, 0))
print(maxi(7, 2, 5))
print(maxi(10, 20, 15))
