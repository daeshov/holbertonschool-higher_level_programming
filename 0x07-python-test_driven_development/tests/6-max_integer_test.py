#/usr/bin/python3
import unittest
max_integer= __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

 def test_values(self):

    self.assertEqual(max_integer("string"), 't')
    self.assertEqual(max_integer([]), None)
    self.assertEqual(max_integer([4]), 4)
    self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    self.assertEqual(max_integer([1.0, 3]), 3)
    self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    self.assertRaises(TypeError, max_integer, 3)
    self.assertRaises(TypeError, max_integer, ["hi", 3, 6, 1])

if __name__ == '__main__':
    unittest.main()
