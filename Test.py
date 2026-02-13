#!/usr/bin/python3
import unittest
from Prog1 import summation

class TestSum(unittest.TestCase):
    def test_add(self):
        self.assertEqual(summation([10, 20]), 30)

if __name__ == "__main__":
    unittest.main()
