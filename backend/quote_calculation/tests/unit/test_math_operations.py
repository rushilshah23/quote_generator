import unittest
from src.utils.math_operations import add, subtract

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)  # Check if 1 + 2 equals 3
        self.assertEqual(add(-1, 1), 0)  # Check if -1 + 1 equals 0
        self.assertEqual(add(0, 0), 0)  # Check if 0 + 0 equals 0

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)  # Check if -1 + -1 equals -2

if __name__ == '__main__':
    unittest.main()