import unittest
import Math

# TODO: tests with 0 and negatives as input!!!

class gcdTests(unittest.TestCase):
    """ Tests for gcd(a, b) (greatest common divisor) function. """
    def tests(self):
        self.assertEqual(Math.gcd(10, 20), 10)
        self.assertEqual(Math.gcd(27, 32), 1)
        self.assertEqual(Math.gcd(12, 40), 4)
        self.assertEqual(Math.gcd(15.0, 20.0), 5)
        self.assertEqual(Math.gcdm(48, 180, 14), 2)

class IsPrimeTests(unittest.TestCase):
    """ Tests for the is_prime() function. """

    primes = [2.0, 3.0, 7.0,
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
        233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 
        2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 
        7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919,
        15817, 21193, 33287, 41017, 51721, 68443, 74453, 81671, 96989, 104729]

    non_primes = [1, 2.5, 6, 18, 30, 105, 37035]

    def test_primes(self):
        """ Prime check for prime numbers. """
        for i in self.primes:
            self.assertTrue(Math.is_prime(i), i)

    def test_non_primes(self):
        """ Prime check for non-prime numbers. """
        for i in self.non_primes:
            self.assertFalse(Math.is_prime(i), i)


class IsSquareTests(unittest.TestCase):
    """ Tests for the is_square() function. """

    squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 
        361, 529, 625, 1024, 1225, 2025, 3600, 4761, 5041, 6561, 6889, 7921,
        8836, 9801, 10000, 10404, 11664, 15376, 23104, 33856, 58081, 123201, 
        215296, 481636, 998001]

    non_squares = [-2, 3, 4.9, 10, 15, 23105]

    def test_squares(self):
        """ Square check for perfect square numbers. """
        for i in self.squares:
            self.assertTrue(Math.is_square(i), i)

    def test_non_squares(self):
        """ Square check for non perfect square numbers. """
        for i in self.non_squares:
            self.assertFalse(Math.is_square(i), i)

class FactorPairsOfTests(unittest.TestCase):
    """ Tests for the factor_pairs_of() function. """
    def tests(self):
        self.assertListEqual(Math.factor_pairs_of(100), [[1, 100], [2, 50], [4, 25], [5, 20], [10, 10]])
        self.assertListEqual(Math.factor_pairs_of(1877), [[1, 1877]])
        self.assertListEqual(Math.factor_pairs_of(1), [[1, 1]])

class ABCFactorsOfTests(unittest.TestCase):
    """ Tests for the abc_factors_of(a, b, c) function. """
    def tests(self):
        self.assertListEqual(Math.abc_factors_of(3, -5, -2), [[1, -6]])
        self.assertListEqual(Math.abc_factors_of(6, 1, -2), [[-3, 4]])
        self.assertListEqual(Math.abc_factors_of(6, -47, 77), [[-14, -33]])

def main():
    unittest.main()

if __name__ == '__main__':
    main()

