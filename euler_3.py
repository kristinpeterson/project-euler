"""
Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 (600,851,475,143)?
"""
import time

start_time = time.time()
############################################

limit = 600851475143

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for x in range(2, limit):
    if limit % x == 0:
        if is_prime(int(limit / x)):
            print("Solution:", int(limit / x))
            break

############################################
print(time.time() - start_time, "seconds")

############################################
# Alternate Solutions
############################################

from math import sqrt
start_time = time.time()
primes = set([2])
value = 3
number = 600851475143
while value < sqrt(number):
    isPrime = True
    for k in primes:
        if value % k == 0:
            isPrime = False
            value += 2
    if isPrime:
        primes.add(value)
        if number % value == 0:
            print(value)
            number /= value
print(number)
print(time.time() - start_time, "seconds")

############################################

start_time = time.time()
n = 600851475143
if n % 2 == 0:
    lastFactor = 2
    n /= 2
    while n % 2 == 0:
        n = n / 2
else:
    lastFactor = 1
factor = 3
maxFactor = sqrt(n)
while n > 1 and factor <= maxFactor:
    if n % factor == 0:
        n = n / factor
        lastFactor = factor
        while n % factor == 0:
            n = n / factor
        maxFactor = sqrt(n)
    factor = factor + 2
if n == 1:
    print(lastFactor)
else:
    print(n)
print(time.time() - start_time, "seconds")