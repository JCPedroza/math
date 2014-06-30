import math

def gcd(a, b):
    """ Return greatest common divisor using Euclid's Algorithm. """
    while b:
        a, b = b, a % b
    return a

def gcdm(*args):
    """ Return greatest common divisior of args using Euclid's Algorithm. """
    return reduce(gcd, args)

def lcm(a, b):
    """ Return lowest common multiple. """
    return a * b / gcd(a, b)

def lcmm(*args):
    """ Return lowest common multiple of args. """
    return reduce(lcm, args)

def factorial(n):
    """ Return factorial of n. """
    acc = 1
    for i in range(1, n + 1): 
        acc *= i
    return acc

def factors_of(n):
    """ Return a set of the factors of n. """
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def is_prime(n):
    """ Check if n is a prime number. """

    if n % 1 != 0:      # Integer check
        return False
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for divisor in xrange(5, 1+int(math.sqrt(n)), 6):
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False

    return True

def is_square(n):
    """ Check if n is a perfect square, based on the Babylonian algorithm. """

    if n % 1 !=0:
        return False
    if n < 0:
        return False
    if n == 1:
        return True

    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen: 
            return False
        seen.add(x)
    return True

def square_factors_of(n):
    """ Return a set of the factors of n that are perfect squares. """
    return set(filter(is_square, factors_of(n)))

