"""
Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time

start_time = time.time()
############################################

# smallest multiple starting at & stepping by 60, eliminates check for 1, 2, 3, 5, 6, 10, 12, 15 & 20
n = 60

while True:
    n += 60
    if n % 4 == 0 and n % 7 == 0 and n % 8 == 0 and n % 9 == 0 and n % 11 == 0 and n % 13 == 0 \
            and n % 14 == 0 and n % 16 == 0 and n % 17 == 0 and n % 18 == 0 and n % 19 == 0:
        break

print("Solution:", n)

############################################
print(time.time() - start_time, "seconds")

############################################
# Alternate Solutions
############################################

# ~2.5x slower than solution from above
n = 60
divisors = [4, 7, 8, 9, 11, 13, 14, 16, 17, 18, 19]
solution_found = False

while solution_found == False:
    n += 60
    for i in divisors:
        if n % i != 0:
            break
        elif i == divisors[len(divisors) - 1]:
            solution_found = True

print("Solution:", n)

# Super Fast Solution
divisors = []

for i in range(1, 21):
    divisors.append(i)

length = len(divisors)

for i in range(1, length):
    for j in range(i-1, 0, -1):
        if divisors[i] % divisors[j] == 0:
            divisors[i] = divisors[i]/divisors[j]

tot = 1
for i in divisors:
    tot *= i
print(divisors)
print(tot)