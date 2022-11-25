#!/usr/bin/python3
# Test case for multiplying two numbers
import unittest

from Program import multiply

class TestMultiply(unittest.TestCase):
    def test1(self):
        data = [40, 80]
        result = multiply(data)
        self.assertEqual(result, 3200)

    def test2(self):
        data = [24, 2]
        result = multiply(data)
        self.assertEqual(result, 48)

    def test3(self):
        data = [50, 2]
        result = multiply(data)
        self.assertEqual(result, 100)


if __name__ == '__main__':
    unittest.main()