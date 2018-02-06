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

def get_largest_factor(n):
    if n % 2 == 0:
        return [n/2, 2]
    sqrt_n_flr = floor(sqrt(n))
    maxnum = sqrt_n_flr - 1 if sqrt_n_flr % 2 == 0 else sqrt_n_flr
    
    for d in range(int(maxnum), -1, -2):
        if n % d == 0:
            return [d, n / d]
        
# taken from Pi Delport's answer at https://stackoverflow.com/questions/3939660
def primes_sieve2(limit):
    a = [True] * limit 
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False


def get_largest_prime_factor(n):
    facs = [n]
    while True:
        curr = facs.pop(0)
        if curr in PRIMES:
            return curr
        facs.extend(get_largest_factor(curr))
        list.sort(facs, reverse=True)
        
N = 600851475143

PRIMES = set(primes_sieve2(500000)) # 500000 > max(get_largest_factor(N))

print get_largest_prime_factor(N)
    
