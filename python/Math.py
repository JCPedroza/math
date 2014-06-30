import math

def gcd(a, b):
    """ Return greatest common divisor using Euclid's Algorithm. """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """ Return lowest common multiple. """
    return a * b / gcd(a, b)

def lcmm(*args):
    """ Return lowest common multiple of args. """
    return reduce(lcm, args)

def factorial(n):
    """ Return factorian of n """
    acc = 1
    for i in range(1, n + 1): 
        acc *= i
    return acc

def is_prime(n):
    """ Is n prime? """

    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit   = int(math.sqrt(n))
    divisor = 5

    while divisor <= limit:
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
        divisor += 6

    return True

def factors(n):
    """ Return a set of the factors of n. """
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))



    
    

