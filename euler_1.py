"""
Multiples of 3 and 5

If we list all the natural numbers below 10
that are multiples of 3 or 5, we get 3, 5, 
6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 
5 below 1000.
"""
import time

start_time = time.time()
############################################

total = 0

for num in range(3, 1000):
    if num % 3 == 0 or num % 5 == 0:
        total += num

print("Solution:", total)


############################################
print(time.time() - start_time, "seconds")

############################################
# Alternate Solutions
############################################

# One liner: 
sum([f for f in range(1, 1000) if not f % 3 or not f % 5])
