import unittest

from number_tester.is_even import is_even


class TestIsEven(unittest.TestCase):
    def test_is_even(self):
        self.assertFalse(is_even.is_even(5))
        self.assertTrue(is_even.is_even(6))
        self.assertTrue(is_even.is_even("10"))
        self.assertFalse(is_even.is_even("hello"))
        self.assertFalse(is_even.is_even([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
