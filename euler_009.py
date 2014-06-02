"""
Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time

start_time = time.time()
############################################

sum = 1000


def is_pythagorean_triplet(a, b, c):
    if a < b and b < c and (a * a) + (b * b) == (c * c):
        return True
    else:
        return False

# Given a + b + c = sum and a < b < c :
#   0 < a <= 334
#   1 < b <= 501
#   334 < c <= 999
def find_triplet_product():
    for a in range(int(sum/3), 0, -1):
        for b in range(int(sum/2), 1, -1):
            c = sum - a - b
            if is_pythagorean_triplet(a, b, c):
                return a * b * c

print("Solution:", find_triplet_product())

############################################
print(time.time() - start_time, "seconds")