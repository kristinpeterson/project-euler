"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

start_time = time.time()
############################################

x = 999
y = 999
largest_palindrome = 0


def is_palindrome(n):
    return str(n) == str(n)[::-1]

while x > 99:
    while y > 99:
        product = x * y
        if is_palindrome(product) and largest_palindrome < product:
            largest_palindrome = product
        y -= 1
    else:
        x -= 1
        y = 999 # reset y value
        continue
    break

print(max)

############################################
print(time.time() - start_time, "seconds")