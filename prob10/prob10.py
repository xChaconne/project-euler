import numpy as np
from time import time

t0 = time()

def prime_sieve(maxval):
    nums = np.ones(maxval).astype(bool)
    nums[0:2] = False
    for i, val in enumerate(nums):
        if val:
            nums[np.arange(2 * i, maxval, i)] = False
    return np.where(nums)[0]
            

print np.sum(prime_sieve(2000000))

t1 = time()

print t1 - t0
