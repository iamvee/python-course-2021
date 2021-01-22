import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False

    return True


def prime_generator():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1


for p in prime_generator():
    print(p)


