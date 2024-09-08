s = 2
e = 20
for num in range(s, e + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(num)
