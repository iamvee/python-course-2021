import time
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False

    return True


t1 = time.time()

primes = []
for i in range(2, 1000):
    if is_prime(i):
        primes.append(i)

t2 = time.time()

print(primes)
print(t2 - t1)