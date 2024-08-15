import unittest

from number_tester.is_number import is_number


class TestIsNumber(unittest.TestCase):
    def test_is_number(self):
        self.assertTrue(is_number.is_number(5))
        self.assertTrue(is_number.is_number(3.14))
        self.assertTrue(is_number.is_number("10"))
        self.assertFalse(is_number.is_number("hello"))
        self.assertFalse(is_number.is_number([1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
