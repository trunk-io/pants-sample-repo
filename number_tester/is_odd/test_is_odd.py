import unittest

from number_tester.is_odd import is_odd


class TestIsOdd(unittest.TestCase):
    def test_is_odd(self):
        self.assertTrue(is_odd.is_odd(5))
        self.assertFalse(is_odd.is_odd(6))
        self.assertFalse(is_odd.is_odd("10"))
        self.assertFalse(is_odd.is_odd("hello"))
        self.assertFalse(is_odd.is_odd([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
