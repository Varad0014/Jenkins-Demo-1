#!/usr/bin/python3
# Test cases for multiplying two numbers
import unittest

from Program import multiply

class TestMultiply(unittest.TestCase):
    def test4(self):
        data = [16, 8]
        result = multiply(data)
        self.assertEqual(result, 48)

    def test5(self):
        data = [6, 8]
        result = multiply(data)
        self.assertEqual(result, 72)

if __name__ == '__main__':
    unittest.main()