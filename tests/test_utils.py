# tests/test_utils.py
import unittest
from src.utils import is_even, is_odd

class TestUtils(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))

    def test_is_odd(self):
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(2))

if __name__ == '__main__':
    unittest.main()
