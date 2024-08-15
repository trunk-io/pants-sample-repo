import unittest

from number_tester.is_prime import is_prime


class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime.is_prime(5))


if __name__ == "__main__":
    unittest.main()
