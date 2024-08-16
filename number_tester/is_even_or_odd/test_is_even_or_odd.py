import unittest

from number_tester.is_even_or_odd.is_even_or_odd import is_even_or_odd


class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_even_or_odd(5), "odd")
        self.assertEqual(is_even_or_odd(6), "even")
        self.assertEqual(is_even_or_odd("a"), "not a number")


if __name__ == "__main__":
    unittest.main()
