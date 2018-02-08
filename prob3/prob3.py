# project euler problem 3
#
# Goal: find the largest factor of a big number N
#
# algorithm outline:
# - initialize a list `facs` as [N]
# - until the largest number in facs is prime, do:
#    - pop first element of facs
#    - split into largest and smallest factor
#    - add to facs
#    - sort facs in descending order


from math import sqrt, floor
from time import time
import numpy as np


def get_largest_factor(n):
    if n % 2 == 0:
        return [n/2, 2]
    sqrt_n_flr = floor(sqrt(n))
    maxnum = sqrt_n_flr - 1 if sqrt_n_flr % 2 == 0 else sqrt_n_flr
    
    # for d in range(int(maxnum), -1, -2):  # probably faster to go in reverse
    for d in range(3, int(maxnum), 2):
        if n % d == 0:
            return [d, n / d]
        

def prime_sieve(maxval):
    nums = np.ones(maxval).astype(bool)
    nums[0:2] = False
    for i, val in enumerate(nums):
        if val:
            nums[np.arange(2 * i, maxval, i)] = False
    return np.where(nums)[0]


def get_largest_prime_factor(n):
    facs = [n]
    while True:
        curr = facs.pop(0)
        if curr in PRIMES:
            return curr
        facs.extend(get_largest_factor(curr))
        list.sort(facs, reverse=True)

t0 = time()

N = 600851475143

PRIMES = set(prime_sieve(500000)) # 500000 > max(get_largest_factor(N))

ans = get_largest_prime_factor(N)
    
t1 = time()

print 'Answer: {}'.format(ans)
print 'Finding factors method: {} milliseconds'.format((t1-t0)* 60.)


