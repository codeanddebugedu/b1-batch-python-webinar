# Q6. Prime numbers in the list
my_list = [4, 8, 6, 5, 3, 12, 1, 3, 15, 10]
prime_list = []
for num in my_list:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
print(prime_list)
