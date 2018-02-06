# taken from Pi Delport's answer at https://stackoverflow.com/questions/3939660
def primes_sieve2(limit):
    a = [True] * limit 
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):
                a[n] = False
                
# Let pi(n) be the prime counting function, i.e.
# pi(n) = |{p <= n : p is prime}|.
# the prime number theorem says that pi(n) ~ n / log(n) as n -> infinity
# we want pi(n) = 10001 so we don't generate any unneccesary primes
# so we want n : n / log(n) = 10000. This n is around 120000 so we'll use that.
# Also if we're only going up to primes at most 120000 in value I think
# this sieve should work fine still.

primelist = list(primes_sieve2(120000))
print primelist[10000]  # 10000 since 0-indexed

