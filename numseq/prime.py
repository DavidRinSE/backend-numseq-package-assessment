import math
def is_prime(m):
    if m == 2:
        return True
    if m%2 == 0 or m == 1:
        return False
    for i in range(3, int(m/2)+1, 2):
        if m % i == 0:
            return False
    return True

def primes(n):
    # Prime numbers using Sieve Algorithm in Python
    primes = [i for i in range(2, n+1)]
    for i in range(2, int(math.sqrt(n))):
        if i in primes:
            for j in range(i*2, n+1, i):
                if j in primes:
                    primes.remove(j)
    return primes

print(primes(1000000))
print(is_prime(5))