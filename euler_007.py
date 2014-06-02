"""
10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""
import time
import math
start_time = time.time()
############################################

i = 3
limit = 10001
primes = [2]


def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

while True:
    if is_prime(i):
        primes.append(i)
    if len(primes) > limit:
        break
    i += 2

print("Solution:", primes[(limit - 1)])

############################################
print(time.time() - start_time, "seconds")

'''
Some useful facts:
- 1 is not a prime
- All primes except 2 are odd
- All primes greater than 3 can be written in the form 6k+/-1
- Any number n can have only one prime factor greater than sqrt(n)
- The consequence for primality testing of a number n is: if we cannot find a number f less than
  or equal sqrt(n) that divides n then n is prime: the only prime factor of n is n itself
'''

# Super Fast Solution

limit = 10001
primes = []
i = 0


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

while True:
    i += 1
    if is_prime(i):
        primes.append(i)
    if len(primes) > limit:
        break

print("Solution:", primes[(limit - 1)])