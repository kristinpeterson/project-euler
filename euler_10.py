"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time
import math

start_time = time.time()
############################################

limit = 2000000
primes = [2]


def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0 or n % (f + 2) == 0:
                return False
            f += 6
    return True

for i in range(3, limit, 2):
    if is_prime(i):
        primes.append(i)

print("Solution:", sum(primes))

############################################
print(time.time() - start_time, "seconds")