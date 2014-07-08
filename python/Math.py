import math, operator

def product(a_list):
    """ Return the product of a list. """
    return reduce(operator.mul, a_list)

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
                ([i, abs(n//i)] for i in range(1, int(abs(n)**0.5) + 1) if n % i == 0)))

def factor_pairs_of(n):
    """ Return a set of the factor pars of n. """
    the_list = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            the_list.append([i, n / i])
    return the_list

def abc_factors_of(a, b, c):
    """ Factors of a * c that together sum b. """
    factors = factor_pairs_of(abs(a * c))
    return_list = []
    for i in factors:
        test_pairs = [i, [i[0]*-1, i[1]*-1], [i[0], i[1]*-1], [i[0]*-1, i[1]]]
        for j in test_pairs:
            if sum(j) == b and product(j) == a * c:
                return_list.append(j)
    return  return_list if len(return_list) > 0 else "none"

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


