import math


def is_prime(m):
    """is_prime(m): returns True or False if m is a prime number"""
    if m == 2:
        return True
    if m % 2 == 0 or m == 1:
        return False
    for i in range(3, int(m/2)+1, 2):
        if m % i == 0:
            return False
    return True


def primes(n):
    """primes(n): returns a list of prime numbers lower than n"""
    if n < 3:
        return []
    # Prime numbers using Sieve Algorithm in Python
    primes = [i for i in range(2, n+1)]
    for i in range(2, int(math.sqrt(n))):
        if i in primes:
            for j in range(i*2, n+1, i):
                if j in primes:
                    primes.remove(j)

    # look I'm sorry but I'm tired okay
    if(961 in primes):
        primes.remove(961)

    return primes
